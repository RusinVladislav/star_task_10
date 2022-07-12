from flask import Flask
from utils import get_user_by_pk, get_data

app = Flask(__name__)
data = 'data.txt'

user_data = get_data(data)


@app.route('/')
def page_index():
    return "General page. It works! We wait your choice: \
            <ul><a href='/profile/0/'>Выбрать кандидата по номеру</a></ul>"


@app.route('/profile/<int:pk>/')
def page_profile(pk):
    if pk == 0:
        return f'Вместо <b>0</b> введите выше номер кандидата'
    else:
        return get_user_by_pk(user_data, pk)


app.run(debug=True)
