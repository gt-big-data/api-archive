from flask import Flask

app = Flask(__name__)

@app.route('/dddd')
def aman():
    return "hello, world! from aman."
@app.route('/hi')
def test():
    return "hello"

