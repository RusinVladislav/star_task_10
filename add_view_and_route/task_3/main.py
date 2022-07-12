from flask import Flask

app = Flask(__name__)
data = {"one": "один", "two": "два", "three": "три"}


@app.route('/')
def page_index():
    return f"General page. It works! We have dict: <p>{data}</p>" \
           f"Выбери нужное действие:" \
           f"<li><a href='/one/'>Страница one</a>" \
           f"<li><a href='/two/'>Страница two</a>" \
           f"<li><a href='/three/'>Страница three</a>"


@app.route('/one/')
def page_first():
    return f"<h2>{data['one']}</h2>"


@app.route('/two/')
def page_two():
    return f"<h2>{data['two']}</h2>"


@app.route('/three/')
def page_three():
    return f"<h2>{data['three']}</h2>"


app.run(debug=True)
