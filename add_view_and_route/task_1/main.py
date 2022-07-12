from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_index():
    return f"General page. It works! We have pages:" \
           f"Выбери нужное действие:" \
           f"<li><a href='/hello/'>Страница hello</a>" \
           f"<li><a href='/goodbye/'>Страница goodbye</a>" \
           f"<li><a href='/seeyou/'>Страница seeyou</a>"


@app.route('/hello/')
def page_hello():
    return f"<h1 align='center'><font size='10' color='green'>hello</h1>"


@app.route('/goodbye/')
def page_goodbye():
    return f"<h1 align='center'><font size='10' color='red'>goodbye</h1>"


@app.route('/seeyou/')
def page_seeyou():
    return f"<h1 align='center'><font size='10' color='blue'>seeyou</h1>"


app.run(debug=True)
