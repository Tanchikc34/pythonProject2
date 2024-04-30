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


# Список профессий
@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', list=list)


# Автоматический ответ
@app.route('/answer')
def answer(list):
    return render_template('list_prof.html', list=list)


# Автоматический ответ
@app.route('/auto_answer/<list>')
def auto_answer(list):
    return render_template('auto_answer.html', list=list)


if __name__ == '__main__':
    app.run(port=8070, host='127.0.0.1')
