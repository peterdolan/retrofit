from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('article.html')

@app.route("/results.html")
def results():
    return render_template('results.html')
