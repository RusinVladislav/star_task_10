from flask import Flask

app = Flask(__name__)
data = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]


@app.route('/')
def page_index():
    return f"General page. It works! We have str: <p>{data}</p>" \
           f"Выбери нужное действие:" \
           f"<li><a href='/mentions/'>Слова, начинающиеся с '@'</a>" \
           f"<li><a href='/words/'>Остальные слова</a>"


@app.route('/mentions/')
def page_mentions():
    result = ', '.join([i for i in data if i[0] == '@'])
    return f"Слова, начинающиеся с символа '@': <b>{result}</b>"


@app.route('/words/')
def page_words():
    result = ', '.join([i for i in data if i[0] != '@'])
    return f"Слова: <b>{result}</b>"


app.run(debug=True)
