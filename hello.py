from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome!"

@app.route("/hi")
def hi():
    return "HI!"

@app.route("/p1")
def p():
    return "this is page 1"

@app.route("/p1/p2")
def p2():
    return "this is page 2"

if __name__ == '__main__':
    app.run()


