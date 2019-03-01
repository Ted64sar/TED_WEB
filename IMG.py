from flask import Flask
from flask import url_for
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    '''<img src="{}" alt="здесь должна была быть картинка, 
           но не нашлась">'''.format(url_for('static', filename='img/Риана.jpg'))

    return "Привет, Яндекс!"


@app.route('/')
@app.route('/image_sample')
def image():
    return '''<img src="/static/img/O.jpeg" alt="здесь у нас многострадальная Риана" >'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')