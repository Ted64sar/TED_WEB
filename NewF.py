from flask import Flask, url_for

i = 0
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/greeting/<username>')
def greeting(username):
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    <title>Привет, {}</title>
                  </head>
                  <body>
                    <h1>Привет, {}!</h1>
                  </body>
                </html>'''.format(username, username)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')