import time
import redis
from flask import Flask
import os

app = Flask(__name__)
# The hostname 'redis' is resolved by Docker Compose to the redis service container
cache = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello, Containerized Quiz App! The database connection works. This page has been viewed {count} times.'

if __name__ == "__main__":
    app.run(debug=True)