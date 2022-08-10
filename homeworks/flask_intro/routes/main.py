from app import app
from flask import render_template


@app.route('/')
def hello_world():
    a = 'Hello, World!'
    return render_template('index.html', variable=a)


@app.route("/sum/<first_num>/<second_num>")
def sum(first_num, second_num):
    result = int(first_num) + int(second_num)
    return render_template('index.html', variable=result)
