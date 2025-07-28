# app.py
from flask import Flask, request
from prometheus_client import generate_latest, Counter, Histogram
import datetime
import logging
import os

app = Flask(__name__)

# --- Logging Setup ---
# Ensure the logs directory exists
log_dir = '/app/logs' # Path inside the Docker container
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, 'app.log')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(threadName)s - %(filename)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler() # Also log to console for Docker logs
    ]
)
logger = logging.getLogger(__name__)

# --- Prometheus Metrics Setup ---
# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint']
)
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP Request Latency',
    ['method', 'endpoint']
)
APP_ERRORS = Counter(
    'app_errors_total',
    'Total application errors',
    ['endpoint']
)

@app.route('/')
def index():
    start_time = datetime.datetime.now()
    method = request.method
    endpoint = '/'
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
    logger.info(f"Access to / from {request.remote_addr}")
    try:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = f"Current Date and Time: {current_time}"
        return response
    except Exception as e:
        APP_ERRORS.labels(endpoint=endpoint).inc()
        logger.error(f"Error processing request to /: {e}", exc_info=True)
        return "An error occurred", 500
    finally:
        end_time = datetime.datetime.now()
        latency = (end_time - start_time).total_seconds()
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(latency)

@app.route('/health')
def health_check():
    # Simple health check endpoint
    logger.info(f"Health check accessed from {request.remote_addr}")
    return "OK"

@app.route('/metrics')
def metrics():
    # Expose Prometheus metrics
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == '__main__':
    # Flask app will run on 0.0.0.0:5000 inside the container
    app.run(host='0.0.0.0', port=5000)

```

```text
# requirements.txt
Flask==2.3.2
prometheus_client==0.17.0
