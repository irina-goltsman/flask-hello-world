# -*- coding: utf-8 -*-
import flask

from app import app


@app.route('/', methods=['GET'])
def get():
    return flask.jsonify("Hello World")
