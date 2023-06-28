from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>i am working in happiest minds</h1>'
