from flask import Flask, jsonify
import logging
from datetime import datetime
import os

app = Flask(__name__)

# Logging setup
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

@app.route('/')
def index():
    current_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    logging.info("Accessed root endpoint.")
    return jsonify({'current_date': current_date})

@app.route('/health/app')
def health_app():
    return jsonify({'status': 'ok'}), 200

@app.route('/health/logs')
def health_logs():
    try:
        with open('logs/app.log', 'r') as f:
            f.read()
        return jsonify({'status': 'log ok'}), 200
    except Exception as e:
        return jsonify({'status': 'log error', 'message': str(e)}), 500

if __name__ == '__main__':
    logging.info("Starting application...")
    app.run(host='0.0.0.0', port=5000)