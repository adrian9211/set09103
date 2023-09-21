from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello'


@app.route('/bye/')
def bye():
    return 'Bye!'


@app.route('/hello/')
def hello():
    return 'Hello Napier!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


