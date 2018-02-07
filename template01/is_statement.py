#encoding: utf-8

from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))
    return "hello world"

@app.route('/login/')
def login():
    return "login"

@app.route('/<is_login>')
def question(is_login):
    if is_login =='1':
        context = {
            "username": "Tim",
            "age": 15,
            "websites": {
                "baidu": "www.baidu.com"
            }
        }
        return render_template('index.html',**context)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)