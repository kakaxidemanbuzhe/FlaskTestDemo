#encoding: utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    avatar = 'http://avatar.csdn.net/B/2/6/2_zjcjava.jpg'
    comments = [
        {
            'user':'Tim',
            'content':'xxxxxxxx'
        },
        {
            'user':'Donnie',
            'content':'yyyyyyyy'
        }
    ]
    return render_template('filter_demo.html', avatar=avatar,comments=comments)

if __name__ == '__main__':
    app.run(debug=True)