import json
import logging
import os
import re
import subprocess
import sys
import tempfile
import time

logger = logging.getLogger(__name__)

PYTHON_EXECUTABLE = sys.executable

TIMEOUT_SECONDS = 10
MAX_OUTPUT_SIZE = 1_000_000
MAX_CODE_SIZE = 50_000

BLOCKED_PATTERNS = [
    r'\bimport\s+os\b', r'\bfrom\s+os\b',
    r'\bimport\s+sys\b', r'\bfrom\s+sys\b',
    r'\bimport\s+subprocess\b', r'\bfrom\s+subprocess\b',
    r'\bimport\s+shutil\b', r'\bfrom\s+shutil\b',
    r'\bimport\s+socket\b', r'\bfrom\s+socket\b',
    r'\bimport\s+http\b', r'\bfrom\s+http\b',
    r'\bimport\s+urllib\b', r'\bfrom\s+urllib\b',
    r'\bimport\s+requests\b',
    r'\bimport\s+signal\b',
    r'\bimport\s+ctypes\b',
    r'\bimport\s+importlib\b',
    r'\bimport\s+pathlib\b',
    r'\bimport\s+glob\b', r'\bfrom\s+glob\b',
    r'\bimport\s+tempfile\b',
    r'\b__import__\s*\(',
    r'\beval\s*\(',
    r'\bexec\s*\(',
    r'\bcompile\s*\(',
]

BLOCKED_PATTERNS_WITH_OPEN = BLOCKED_PATTERNS + [r'\bopen\s*\(']


def _get_sandbox_config():
    """Get sandbox configuration from Flask app config or defaults."""
    try:
        from flask import current_app
        return {
            'mode': current_app.config.get('SANDBOX_MODE', 'subprocess'),
            'image': current_app.config.get('SANDBOX_IMAGE', 'pythonlearning-sandbox:latest'),
            'timeout': current_app.config.get('SANDBOX_TIMEOUT', TIMEOUT_SECONDS),
            'memory_limit': current_app.config.get('SANDBOX_MEMORY_LIMIT', '256m'),
        }
    except (RuntimeError, ImportError):
        return {
            'mode': 'subprocess',
            'image': 'pythonlearning-sandbox:latest',
            'timeout': TIMEOUT_SECONDS,
            'memory_limit': '256m',
        }


def check_blocked_patterns(code, allow_file_io=False):
    patterns = BLOCKED_PATTERNS if allow_file_io else BLOCKED_PATTERNS_WITH_OPEN
    for pattern in patterns:
        match = re.search(pattern, code)
        if match:
            return f"Blocked: '{match.group()}' is not allowed in this assignment."
    return None


# ── Docker Sandbox ──────────────────────────────────────────────────────

def _run_docker(tmpdir, command, stdin_input='', timeout=10, sandbox_cfg=None):
    """Run code in an isolated Docker container."""
    try:
        import docker as docker_sdk
    except ImportError:
        logger.error("Docker SDK not installed. Falling back to subprocess.")
        return None  # Signal to caller to fall back

    if sandbox_cfg is None:
        sandbox_cfg = _get_sandbox_config()

    try:
        client = docker_sdk.from_env()
    except Exception as e:
        logger.error(f"Cannot connect to Docker: {e}. Falling back to subprocess.")
        return None

    container = None
    try:
        container = client.containers.run(
            sandbox_cfg['image'],
            command=command,
            volumes={tmpdir: {'bind': '/sandbox', 'mode': 'rw'}},
            working_dir='/sandbox',
            network_disabled=True,
            mem_limit=sandbox_cfg['memory_limit'],
            cpu_period=100000,
            cpu_quota=50000,  # 50% of one CPU
            pids_limit=64,
            read_only=False,
            detach=True,
            user='sandbox',
        )

        exit_info = container.wait(timeout=timeout)
        stdout = container.logs(stdout=True, stderr=False).decode('utf-8', errors='replace')
        stderr = container.logs(stdout=False, stderr=True).decode('utf-8', errors='replace')

        return {
            'status': 'completed',
            'stdout': stdout[:MAX_OUTPUT_SIZE],
            'stderr': stderr[:MAX_OUTPUT_SIZE],
            'returncode': exit_info.get('StatusCode', 1),
        }
    except Exception as e:
        err_str = str(e).lower()
        if 'timeout' in err_str or 'timed out' in err_str or 'read timed out' in err_str:
            return {'status': 'timeout', 'error': f'Code execution exceeded {timeout} seconds.'}
        logger.error(f"Docker sandbox error: {e}")
        return {'status': 'error', 'error': f'Sandbox error: {str(e)[:200]}'}
    finally:
        if container:
            try:
                container.remove(force=True)
            except Exception:
                pass


# ── Subprocess Sandbox (original) ──────────────────────────────────────

def _run_subprocess(code_file, tmpdir, stdin_input='', timeout=TIMEOUT_SECONDS):
    """Run code via local subprocess (development/fallback mode)."""
    try:
        result = subprocess.run(
            [PYTHON_EXECUTABLE, code_file],
            input=stdin_input,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=tmpdir,
            env={
                'PATH': os.path.dirname(PYTHON_EXECUTABLE) + ':/usr/bin:/usr/local/bin',
                'HOME': tmpdir,
                'PYTHONDONTWRITEBYTECODE': '1',
            },
        )
        return {
            'status': 'completed',
            'stdout': result.stdout[:MAX_OUTPUT_SIZE],
            'stderr': result.stderr[:MAX_OUTPUT_SIZE],
            'returncode': result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'error': f'Code execution exceeded {timeout} seconds.'}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}


def _run_subprocess_tests(test_file, tmpdir, timeout=TIMEOUT_SECONDS * 2):
    """Run pytest via local subprocess (development/fallback mode)."""
    try:
        result = subprocess.run(
            [PYTHON_EXECUTABLE, '-m', 'pytest', test_file, '-v', '--tb=short', '-q'],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=tmpdir,
            env={
                'PATH': os.path.dirname(PYTHON_EXECUTABLE) + ':/usr/bin:/usr/local/bin',
                'HOME': tmpdir,
                'PYTHONDONTWRITEBYTECODE': '1',
                'PYTHONPATH': tmpdir,
            },
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return None  # Timeout
    except Exception as e:
        return str(e)


# ── Public API ──────────────────────────────────────────────────────────

def run_student_code(code, stdin_input='', timeout=TIMEOUT_SECONDS, allow_file_io=False, sandbox_files=None):
    if len(code) > MAX_CODE_SIZE:
        return {'status': 'error', 'error': 'Code exceeds maximum size limit (50KB).'}

    # Always do regex check as first-pass defense (even in Docker mode)
    blocked = check_blocked_patterns(code, allow_file_io)
    if blocked:
        return {'status': 'error', 'error': blocked}

    sandbox_cfg = _get_sandbox_config()

    with tempfile.TemporaryDirectory() as tmpdir:
        code_file = os.path.join(tmpdir, 'student_code.py')
        with open(code_file, 'w') as f:
            f.write(code)

        if sandbox_files:
            for filename, content in sandbox_files.items():
                filepath = os.path.join(tmpdir, filename)
                with open(filepath, 'w') as f:
                    f.write(content)

        # Try Docker mode first
        if sandbox_cfg['mode'] == 'docker':
            result = _run_docker(
                tmpdir,
                command=['python', '/sandbox/student_code.py'],
                stdin_input=stdin_input,
                timeout=sandbox_cfg['timeout'],
                sandbox_cfg=sandbox_cfg,
            )
            if result is not None:
                return result
            logger.warning("Docker sandbox unavailable, falling back to subprocess")

        # Subprocess mode (default or fallback)
        return _run_subprocess(code_file, tmpdir, stdin_input, timeout)


def run_test_cases(code, test_cases_code, allow_file_io=False):
    sandbox_cfg = _get_sandbox_config()

    with tempfile.TemporaryDirectory() as tmpdir:
        code_file = os.path.join(tmpdir, 'student_code.py')
        with open(code_file, 'w') as f:
            f.write(code)

        test_file = os.path.join(tmpdir, 'test_student.py')
        with open(test_file, 'w') as f:
            f.write(test_cases_code)

        raw_output = None

        # Try Docker mode first
        if sandbox_cfg['mode'] == 'docker':
            result = _run_docker(
                tmpdir,
                command=['python', '-m', 'pytest', '/sandbox/test_student.py', '-v', '--tb=short', '-q'],
                timeout=sandbox_cfg['timeout'] * 2,
                sandbox_cfg=sandbox_cfg,
            )
            if result is not None:
                if result['status'] == 'timeout':
                    return {
                        'passed': 0,
                        'total': 0,
                        'details': [{'name': 'timeout', 'status': 'TIMEOUT', 'message': 'Tests timed out.'}],
                        'raw_output': 'Test execution timed out.',
                    }
                raw_output = (result.get('stdout', '') + result.get('stderr', ''))[:MAX_OUTPUT_SIZE]
            else:
                logger.warning("Docker sandbox unavailable for tests, falling back to subprocess")

        # Subprocess mode (default or fallback)
        if raw_output is None:
            output = _run_subprocess_tests(test_file, tmpdir, TIMEOUT_SECONDS * 2)
            if output is None:
                return {
                    'passed': 0,
                    'total': 0,
                    'details': [{'name': 'timeout', 'status': 'TIMEOUT', 'message': 'Tests timed out.'}],
                    'raw_output': 'Test execution timed out.',
                }
            raw_output = output

        passed, total, details = parse_pytest_output(raw_output)
        return {
            'passed': passed,
            'total': total,
            'details': details,
            'raw_output': raw_output[:MAX_OUTPUT_SIZE],
        }


def parse_pytest_output(output):
    details = []
    passed = 0
    total = 0

    for line in output.split('\n'):
        if '::' in line and ('PASSED' in line or 'FAILED' in line or 'ERROR' in line):
            total += 1
            test_name = line.split('::')[-1].split(' ')[0].strip()
            if 'PASSED' in line:
                passed += 1
                details.append({'name': test_name, 'status': 'PASSED', 'message': ''})
            elif 'FAILED' in line:
                details.append({'name': test_name, 'status': 'FAILED', 'message': line.strip()})
            elif 'ERROR' in line:
                details.append({'name': test_name, 'status': 'ERROR', 'message': line.strip()})

    if total == 0:
        passed_match = re.search(r'(\d+) passed', output)
        failed_match = re.search(r'(\d+) failed', output)
        error_match = re.search(r'(\d+) error', output)
        p = int(passed_match.group(1)) if passed_match else 0
        f = int(failed_match.group(1)) if failed_match else 0
        e = int(error_match.group(1)) if error_match else 0
        passed = p
        total = p + f + e
        if total > 0 and not details:
            for i in range(p):
                details.append({'name': f'test_{i+1}', 'status': 'PASSED', 'message': ''})
            for i in range(f):
                details.append({'name': f'test_failed_{i+1}', 'status': 'FAILED', 'message': 'Test failed'})
            for i in range(e):
                details.append({'name': f'test_error_{i+1}', 'status': 'ERROR', 'message': 'Test error'})

    return passed, total, details


def normalize_output(text):
    lines = text.strip().split('\n')
    return '\n'.join(line.rstrip() for line in lines)


def compute_score(passed_tests, total_tests, output_matches, output_total,
                  test_weight=0.6, output_weight=0.4, max_score=100):
    test_pct = (passed_tests / total_tests) if total_tests > 0 else 0.0
    output_pct = (output_matches / output_total) if output_total > 0 else 0.0
    raw_score = max_score * (test_weight * test_pct + output_weight * output_pct)
    return round(raw_score, 1)


def validate_submission(code, assignment):
    result = {
        'status': 'completed',
        'score': 0.0,
        'passed_tests': 0,
        'total_tests': 0,
        'test_details': [],
        'output_matches_count': 0,
        'output_total_count': 0,
        'output_match': False,
        'actual_output': '',
        'error_message': '',
        'execution_time_ms': 0,
    }

    start_time = time.time()
    allow_file_io = getattr(assignment, 'allow_file_io', False)

    # Phase 1: Output comparison
    try:
        io_pairs = json.loads(assignment.input_output_pairs)
    except (json.JSONDecodeError, TypeError):
        io_pairs = []

    result['output_total_count'] = len(io_pairs)
    outputs = []

    for pair in io_pairs:
        run_result = run_student_code(
            code,
            stdin_input=pair.get('input', ''),
            allow_file_io=allow_file_io,
        )
        if run_result['status'] == 'error':
            result['error_message'] = run_result.get('error', '')
            result['status'] = 'error'
            outputs.append(f"ERROR: {result['error_message']}")
            continue
        if run_result['status'] == 'timeout':
            result['error_message'] = run_result.get('error', 'Timeout')
            result['status'] = 'timeout'
            outputs.append('TIMEOUT')
            continue

        actual = run_result['stdout'].strip()
        expected = pair['expected_output'].strip()
        outputs.append(actual)

        if run_result.get('stderr') and run_result['returncode'] != 0:
            result['error_message'] = run_result['stderr'][:500]
            continue

        if normalize_output(actual) == normalize_output(expected):
            result['output_matches_count'] += 1

    result['actual_output'] = '\n---\n'.join(outputs)
    result['output_match'] = (
        result['output_matches_count'] == result['output_total_count']
        and result['output_total_count'] > 0
    )

    # Phase 2: Test case execution
    if assignment.test_cases_code and assignment.test_cases_code.strip():
        test_result = run_test_cases(code, assignment.test_cases_code, allow_file_io)
        result['passed_tests'] = test_result['passed']
        result['total_tests'] = test_result['total']
        result['test_details'] = test_result['details']
        if not result['error_message'] and test_result.get('raw_output'):
            for detail in test_result['details']:
                if detail['status'] in ('FAILED', 'ERROR') and detail['message']:
                    result['error_message'] = detail['message']
                    break

    # Compute score
    result['execution_time_ms'] = int((time.time() - start_time) * 1000)
    result['score'] = compute_score(
        passed_tests=result['passed_tests'],
        total_tests=result['total_tests'],
        output_matches=result['output_matches_count'],
        output_total=result['output_total_count'],
        test_weight=assignment.test_weight,
        output_weight=assignment.output_weight,
        max_score=assignment.max_score,
    )

    if result['status'] not in ('error', 'timeout'):
        result['status'] = 'completed'

    return result
