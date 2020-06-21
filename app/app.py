from flask import Flask

meu_web_app = Flask('meu_web_app')


@meu_web_app.route('/')
def pagina_inicial():
    return "ok"


@meu_web_app.route('/hello')
def hello_world():
    return "Hello World"

@meu_web_app.route('/name')
def name():
    return "you name"

if __name__ == "__main__":
    meu_web_app.run(debug=True)
