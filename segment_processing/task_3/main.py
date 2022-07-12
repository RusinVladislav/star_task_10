from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_index():
    return "General page. It works! We wait your choice: \
            <li><a href='/to_bytes/0'>перевести в байты</a></li> \
            <li><a href='/to_kbytes/0'>перевести в килобайты</a></li>"


@app.route('/to_kbytes/<int:number>/')
def page_to_kbytes(number):
    if number != 0:
        result = number * 1024
        return f'В <b>{number}</b> мегабайте - <b>{result}</b> килобайт'
    else:
        return 'Введите число отличное от <b>0<b>'


@app.route('/to_bytes/<int:number>/')
def page_to_bytes(number):
    if number != 0:
        result = number * 1024 * 1024
        return f'В <b>{number}</b> мегабайте - <b>{result}</b> байт'
    else:
        return 'Введите число отличное от <b>0<b>'


app.run(debug=True)
