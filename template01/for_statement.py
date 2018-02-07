#encoding: utf-8

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = {
        'username':'Tim',
        'age':18
    }
    websites = ['baidu','google']
    return render_template('for_statement.html',user=user,websites=websites)

if __name__ == '__main__':
    app.run(debug=True)