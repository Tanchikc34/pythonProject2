from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def root():
    return "<h1 style=color:rgb(200,0,0)>Миссия Колонизация Марса</h1>"


@app.route('/index')
def index():
    return "<h1 style=color:rgb(0,200,0)>И на Марсе будут яблони цвести!</h1>"


@app.route('/promotion')
def promotion():
    promotion_list = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                      "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '<br>'.join(promotion_list)


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
                    <title>Привет, Яндекс!</title>
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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
