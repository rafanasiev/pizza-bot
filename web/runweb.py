#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from bottle import Bottle, request, route, template, error, run

# app
app = Bottle()

@app.error(404)
def error404(error):
    return "No good!"

@app.route('/')
def index():
    return template('index.tp', request=request)

@app.route('/pizza-bot')
def hello():
    name = request.cookies.username or 'Guest'
    return template("Hello {{name}}, waiting for the order...", name=name)

run(app, host='localhost', port=8080, reloader=True, debug=True)
