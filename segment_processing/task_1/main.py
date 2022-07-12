from flask import Flask

app = Flask(__name__)
data = """На крыльце сидел котейка
          Мимо шел казах Андрейка
          Будет завтра у Андрейки
          из котейки тюбетейка
          
          В лесу родилась елочка
          В лесу она росла
          Зимой и летом стройная
          Зеленая была"""


@app.route('/')
def page_index():
    return f"General page. It works! We have: <pre>{data}</pre>"


@app.route('/find/<word>/')
def page_city(word):
    if word.strip().lower() in data.lower():
        return f"<b>ДА!</b> Слово <b>{word}</b> найдено"
    else:
        return f"<b>НЕТ!</b> Слово <b>{word}</b> не найдено"


app.run(debug=True)
