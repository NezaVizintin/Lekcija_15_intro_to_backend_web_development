import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hw_index.html")

@app.route("/about")
def about():
    return render_template("hw_about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("hw_portfolio.html")

@app.route("/portfolio/hair-salon")
def hair_salon():
    return render_template("hair_salon_index.html")

if __name__ == "__main__":
    app.run(use_reloader=True)