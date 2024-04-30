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
@app.route('/answer/<title>/<surname>/<name>/<education>/<profession>/<sex>/<motivation>/<ready>')
def answer(title, surname, name, education, profession, sex, motivation, ready):
    list = {}
    list['title'] = title
    list['surname'] = surname
    list['name'] = name
    list['education'] = education
    list['profession'] = profession
    list['sex'] = sex
    list['motivation'] = motivation
    list['ready'] = ready
    return render_template('list_prof.html', list=list)


# Автоматический ответ
@app.route('/auto_answer')
def auto_answer():
    list = {}
    list['title'] = "Анкета"
    list['surname'] = "Гут"
    list['name'] = "Макс"
    list['education'] = "высшее"
    list['profession'] = "Капитан корабля"
    list['sex'] = "М"
    list['motivation'] = "Всегда мечтал застрять на Марсе!"
    list['ready'] = "Да"
    return render_template('auto_answer.html', **list)


# Двойная защита
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Аварийный доступ', form=form)


# По каютам!
@app.route('/distribution')
def distribution():
    spisok = ["Марк", "Энди", "Клаус", "Мэт"]
    # spisok = input().split(" ")
    return render_template('distribution.html', spisok=spisok)


# Цвет каюты
@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=age)


# Галерея с загрузкой
@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    folder_path = 'static/img/car_i/'
    files = os.listdir(folder_path)
    print(files)
    if request.method == 'POST':
        f = request.files['file']
        f.save(f"static/img/car_i/{f.filename}")
        return redirect('/carousel')
    return render_template('carousel.html', title='Марс?', files=files)


if __name__ == '__main__':
    app.run(port=8070, host='127.0.0.1')
