#!/usr/bin/env python
# coding=utf-8
# author: xsl

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "hello leancloud"

@app.route("/xiu")
def xiu():
    return "<a href=\"http://www.insword.cn\">insword</a>"

@app.route("/test", methods=['POST'])
def test():
    data = request.json.get('test') or "no data"
    return jsonify({"data":data})

if __name__ == "__main__":
    app.run()
