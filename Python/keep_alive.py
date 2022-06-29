from flask import flask
from threading import Thread

app = flask('')

@app.route('/')
def home():
    return "Hello. This is Bot, I am Alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()