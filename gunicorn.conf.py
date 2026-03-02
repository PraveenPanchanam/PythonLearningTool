import multiprocessing
import os

# Bind
bind = '0.0.0.0:' + os.environ.get('PORT', '8000')

# Workers: for a classroom app, 2-4 is sufficient
workers = int(os.environ.get('WEB_WORKERS', min(multiprocessing.cpu_count() * 2 + 1, 4)))
worker_class = 'gthread'
threads = 2

# Timeout: set higher because code submissions can take time
timeout = 120
graceful_timeout = 30

# Logging
accesslog = '-'  # stdout
errorlog = '-'   # stderr
loglevel = os.environ.get('LOG_LEVEL', 'info').lower()

# Security
limit_request_line = 8190
limit_request_fields = 100
limit_request_field_size = 8190

# Preload for faster worker startup
preload_app = True
