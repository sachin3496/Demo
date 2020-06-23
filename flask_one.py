from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='color:red'> Welcome to first Web Page Powered by Falsk<h1> <a href='/hello'>Hello</a>"

@app.route("/hello/")
def hello():
    return "<h1 style='color:blue'>Hello World</h1><a href='/'>HOME</a>"

app.run('localhost', 80)
