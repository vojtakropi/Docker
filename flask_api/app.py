import os

import requests
from flask import Flask, render_template, request
import json

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/fileinput", methods=["GET"])
def fileinput():
    return render_template("inputfile.html")


@app.route("/fileinput", methods=["POST"])
def fileinput_file():
    profile = request.files["avatar"]
    url = 'http://docker-new_app-1:3000/getfile'
    t = profile.stream.read()
    t = t.decode("utf-8")
    myobj = {'text': t,
             'filename': profile.filename}

    requests.post(url, json=myobj)
    return render_template("inputfile.html")

@app.route("/getocurences")
def get_occurences():
    url = 'http://docker-new_app-1:3000/getcounts'
    x = requests.get(url)
    data = x.content.decode("utf-8")
    data = json.loads(data)
    return  render_template('showcount.html', data=data['results'])



if __name__ == "__main__":
    app.run(debug=True, port=5000)


