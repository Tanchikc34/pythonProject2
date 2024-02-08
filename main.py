from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def root():
    return "<h1 style=color:rgb(200,0,0)>Миссия Колонизация Марса</h1>"


# Колонизация Марса
@app.route('/index')
def index():
    return "<h1 style=color:rgb(0,200,0)>И на Марсе будут яблони цвести!</h1>"


# Рекламная кампания
@app.route('/promotion')
def promotion():
    promotion_list = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                      "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '<br>'.join(promotion_list)


# Изображение Марса
@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="https://klike.net/uploads/posts/2023-01/1674455123_3-61.jpg" alt="<Альтернативный текст для изображения>" width="450" height="300">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


# Реклама с картинкой
@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                     rel="stylesheet" 
                     integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" 
                     crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/image.jpg')}" alt="<Альтернативный текст для изображения>" width="450" height="300">
                    <br><br>
                    <p class="bg-success p-2 text-white">Человечество вырастает из детства.</p>
                    <p class="bg-danger p-2 text-white">Человечеству мала одна планета.</p>
                    <p class="bg-primary p-2 text-white">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="bg-warning p-2 text-black">И начнем с Марса!</p>
                    <p class="bg-info p-2 text-black">Присоединяйся!</p>
                  </body>
                </html>'''


# Отбор астронавтов
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                             rel="stylesheet" 
                             integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" 
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                                    <h1 class="title">Анкета претендента</h1>
                                    <h4 class="title">на участие в миссии</h4>
                                    <div>
                                        <form class="login_form" method="post">
                                            <input type="text" class="form-control margin" placeholder="Введите фамилию" aria-label="Фамилия">
                                            <input type="text" class="form-control margin" placeholder="Введите имя" aria-label="Имя">
                                            <input type="email" class="form-control margin" placeholder="Введите адрес почты">
                                            <div class="form-group margin">
                                                <label for="classSelect">Какое у вас образование?</label>
                                                <select class="form-control" id="classSelect" name="class">
                                                  <option>Начальное общее</option>
                                                  <option>Основное общее</option>
                                                  <option>Среднее общее</option>
                                                  <option>Среднее профессиональное</option>
                                                  <option>Высшее I степени</option>
                                                  <option>Высшее II степени</option>
                                                  <option>Высшее III степени</option>
                                                </select>
                                            </div>
                                            
                                            <div class="form-group margin">
                                                <label for="form-check">Какие у Вас есть профессии?</label>
                                                <div class="form-group row">
                                                <div>
                                                <input type="checkbox" class="form-check-input" id="i1">
                                                <label class="form-check-label" for="i1">Инженер-исследователь</label>
                                                </div>
                                                <div>
                                                <input type="checkbox" class="form-check-input" id="i2">
                                                <label class="form-check-label" for="i2">Астрогеолог</label>
                                                </div>
                                                <div>
                                                <input type="checkbox" class="form-check-input" id="i3">
                                                <label class="form-check-label" for="i3">Метеоролог</label>
                                                </div>
                                                </div>
                                            </div>
                                            
                                            <div class="form-group margin">
                                                <label for="form-check">Укажите пол</label>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                                  <label class="form-check-label" for="male">
                                                    Мужской
                                                  </label>
                                                </div>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                                  <label class="form-check-label" for="female">
                                                    Женский
                                                  </label>
                                                </div>
                                            </div>
                                            <div class="form-group margin">
                                                <label for="about">Почему Вы хотите принять участие миссии?</label>
                                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                            </div>
                                            <div class="form-group margin">
                                                <label for="photo">Приложите фотографию</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                            
                                            <div class="form-group form-check margin">
                                                <input type="radio" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                            </div>
                                            
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                        </form>
                                    </div>
                                  </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


# Варианты выбора
@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                     rel="stylesheet" 
                     integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" 
                     crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <p>Планета - это большое округлое астрономическое тело.</p>
                    <p class="bg-success p-2 text-white">Планетами (др.-греч. πλανήτης, от др.-греч. πλάνης — «странник») греки называли т.н. «блуждающие звёзды».</p>
                    <p class="bg-danger p-2 text-white">По мере развития науки представления о планетах менялись в немалой степени и благодаря открытию новых объектов и обнаружению различий между ними.</p>
                    <p class="bg-primary p-2 text-white">По состоянию на 16 июня 2022 года достоверно подтверждено существование 5098 экзопланет в 3770 планетных системах, из которых в 825 имеется более одной планеты.</p>
                    <p class="bg-warning p-2 text-black"> Размеры известных экзопланет лежат в пределах от размеров планет земной группы до более крупных, чем планеты-гиганты!</p>
                  </body>
                </html>'''


# Пейзажи Марса
@app.route('/cat')
def cat():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                     rel="stylesheet" 
                     integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" 
                     crossorigin="anonymous">
                    <title>Пейзажи Марса</title>
                  </head>
                  <body>
                    <h1>Котики!</h1>
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="{url_for('static', filename='img/img.png')}" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="{url_for('static', filename='img/img_1.png')}" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="{url_for('static', filename='img/img_2.png')}" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
