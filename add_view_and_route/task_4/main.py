from flask import Flask

app = Flask(__name__)
data = [23, 16, 144, 72, 90, 11, 5]


@app.route('/')
def page_index():
    return f"General page. It works! We have list: <p>{data}</p>" \
           f"Выбери нужное действие:" \
           f"<li><a href='/first/'>Первое число в списке</a>" \
           f"<li><a href='/last/'>Последнее число в списке</a>" \
           f"<li><a href='/get_number/0'>Выбрать число из списка</a>" \
           f"<li><a href='/sum/'>Сумма всех чисел в списке</a>"


@app.route('/first/')
def page_first():
    return f"Первое число: <b>{data[0]}</b>"


@app.route('/last/')
def page_last():
    return f"Последнее число: <b>{data[-1]}</b>"


@app.route('/get_number/<int:number>')
def page_get_number(number):
    if number == 0 or number > len(data):
        return f"В нашем списке нет запрашиваемого числа, выберите одно из {len(data)}"
    else:
        return f"Число №{number} равно: <b>{data[number - 1]}</b>"


@app.route('/sum/')
def page_sum():
    return f"Сумма чисел: <b>{sum(data)}</b>"


app.run(debug=True)
