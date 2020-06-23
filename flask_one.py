from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/hello/")
def hello():
    return "<h1 style='color:blue'>Hello World</h1><a href='/'>HOME</a>"

app.run('localhost', 80)
