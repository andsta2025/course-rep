from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)

# Configure simple in-memory cache
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 60  # 60 seconds
cache = Cache(app)

@app.route('/slow')
@cache.cached()
def slow_response():
    start = time.time()
    time.sleep(3)  # Expensive work
    end = time.time()
    duration = round(end - start, 2)
    return jsonify(message="Slow response (cached)", load_time=duration)

if __name__ == '__main__':
    app.run(debug=True)
