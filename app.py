from flask import Flask
import redis

app = Flask("myapp")
cache = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
 count = cache.incr("visits")
 return "Hello from inside a Docker container! Visit count: " + str(count)

app.run(host="0.0.0.0", port=5000)
