from flask import Flask
from random import choice

app = Flask(__name__)


@app.route('/')
def page_index():
    return f"General page. It works! We have page: " \
           f"<li><a href='/random/'>Хочешь узнать свое счастливое число? ЖМИ СКОРЕЙ!</a>"


@app.route('/random/')
def page_first():
    return f"<h1 align='center'>{choice(range(1, 10))}</h1>"


app.run(debug=True)
