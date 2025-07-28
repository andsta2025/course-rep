from flask import Flask
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/')
def index():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"Accessed root endpoint, time: {current_time}")
    return f"Current server date and time is: {current_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
