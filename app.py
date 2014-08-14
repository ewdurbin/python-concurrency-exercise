
import json
import random
import time
import uuid

from flask import Flask
from flask import Response
from flask import jsonify

def feed_poll():
    time.sleep(random.randint(0, 5))
    return {"updates": None}

app = Flask(__name__)

@app.route('/')
def root_route():
    return jsonify({"Title": "Concurrency is hard, let's go shopping!"})

@app.route('/hash_me')
def hash_me():
    return jsonify({"uuid4": uuid.uuid4()})

@app.route('/check_feed')
def check_feed():
    return jsonify(feed_poll())

@app.route('/stream_feed')
def stream_feed():
    def generate():
        while True:
            yield json.dumps(feed_poll()) + "\n"
    return Response(generate())
