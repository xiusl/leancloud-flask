#!/usr/bin/env python
# coding=utf-8
# author: xsl

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello leancloud"

@app.route("/xiu")
def xiu():
    return "<a href=\"http://www.insword.cn\">insword</a>"
