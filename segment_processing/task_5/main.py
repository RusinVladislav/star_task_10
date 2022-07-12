from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_index():
    return f"General page. It works! We wait your choice: \
            <ul><a href='/meal/ничего/ничего/ничего/'>Ваш рацион на сегодня</a></ul>"


@app.route('/meal/<first>/<second>/<three>/')
def page_meal(first, second, three):
    if first == second == three == 'ничего':
        return f"<p>Введите выше через '/', что вы хотите на первое, второе и третье</p>"
    else:
        return f"<p>На первое: {first}</p> \
                 <p>На второе: {second}</p> \
                 <p>На третье: {three}</p> \
                 <p>Приятного аппетита!</p>"


app.run(debug=True)
