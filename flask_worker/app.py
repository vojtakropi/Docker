import os

from flask import Flask, request
from dataworker import countMarek, getcount, checkDB
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/getfile", methods=["POST"])
def getfile():
    data = json.loads(request.data)
    text = data['text']
    filename = data['filename']
    countMarek(filename, text)
    return "procesed"


@app.route("/test")
def test():
    checkDB()
    return "look"


@app.route("/getcounts")
def getcounts():
    return getcount()


if __name__ == "__main__":
    app.run(debug=True, port=3000)
