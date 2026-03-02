FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    FLASK_CONFIG=production

WORKDIR /app

# Install system dependencies for psycopg and building wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc g++ \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (separate step for Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove gcc g++ \
    || true

# Copy application code
COPY . .

# Create non-root user and necessary directories
RUN groupadd -r appuser && useradd -r -g appuser appuser \
    && mkdir -p /app/logs /app/instance \
    && chown -R appuser:appuser /app

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

USER appuser

# Expose port
EXPOSE 8000

# Health check with longer start period for Render cold starts
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=5 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/')" || exit 1

# Run with entrypoint (migrations + Gunicorn)
CMD ["./entrypoint.sh"]
