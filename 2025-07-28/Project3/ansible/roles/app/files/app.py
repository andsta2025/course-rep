from flask import Flask, request
from datetime import datetime
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/')
def index():
    now = datetime.utcnow().isoformat()
    logging.info(f"Accessed by {request.remote_addr} - Time: {now}")
    return f"Current date (UTC): {now}"

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Error: {e}", exc_info=True)
    return "An error occurred", 500

# 🔥 Svarbu: paleisti serverį
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)