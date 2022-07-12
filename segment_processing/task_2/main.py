from flask import Flask

app = Flask(__name__)
data = {1: "Минск", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород", 7: "Киев"}


@app.route('/')
def page_index():
    return f"General page. It works! We have: <p>{data}</p>"


@app.route('/city/<int:number>/')
def page_city(number):
    return data.get(number)


app.run(debug=True)
