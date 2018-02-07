from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    class Person(object):
        name = "lulu"
        age = 12
    p = Person()

    context = {
        "username":"Tim",
        "age":15,
        "person":p,
        "websites":{
            "baidu":"www.baidu.com"
        }
    }

    return render_template('if_statement.html',**context)


if __name__ == '__main__':
    app.run(debug=True)