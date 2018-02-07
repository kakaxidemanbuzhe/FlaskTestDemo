#encoding: utf-8

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))
    return "hello world"

@app.route('/login/')
def login():
    return "login"

@app.route('/question/<is_login>')
def question(is_login):
    if is_login =='1':
        return "question"
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)