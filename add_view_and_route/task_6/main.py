from flask import Flask

app = Flask(__name__)
data = "Кот это не хлеб, подумай, но не ешь его, разработчик! Ай, ну я же просил. Ну, что-ж будь что будет"


@app.route('/')
def page_index():
    return f"General page. It works! We have str: <p>{data}</p>" \
           f"Выбери нужное действие:" \
           f"<li><a href='/words/'>Всего слов</a>" \
           f"<li><a href='/spaces/'>Всего пробелов</a>" \
           f"<li><a href='/letters/'>Всего букв</a>"


@app.route('/words/')
def page_words():
    return f"Всего слов: <b>{data.count(' ') + 1}</b>"


@app.route('/spaces/')
def page_spaces():
    return f"Всего пробелов: <b>{data.count(' ')}</b>"


@app.route('/letters/')
def page_letters():
    letters = 0
    for i in data:
        if i.isalpha():
            letters += 1
    return f"Всего букв: <b>{letters}</b>"


app.run(debug=True)
