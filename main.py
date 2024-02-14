from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def route():
    param = {'title': 'Домашняя страница'}
    return render_template('base.html', **param)


# Готовимся к миссии
@app.route('/index/<name>')
def index(name):
    param = {'title': name}
    return render_template('base.html', **param)


# Тренировки в полёте
@app.route('/training/<prof>')
def training(prof):
    param = {'title': 'Тренировка', 'prof': prof}
    return render_template('training.html', **param)


if __name__ == '__main__':
    app.run(port=8070, host='127.0.0.1')
