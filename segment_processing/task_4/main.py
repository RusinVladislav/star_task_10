from flask import Flask

app = Flask(__name__)
records = []


@app.route('/')
def page_index():
    return f"General page. It works! We have: <p>{records}</p>"


@app.route('/add/<word>/')
def page_add_word(word):
    records.append(word)
    return f'Слово <b>{word}</b> добавлено'


@app.route('/show/')
def page_show():
    return ' '.join(records)


app.run(debug=True)
