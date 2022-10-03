from flask import Flask, render_template

app = Flask(__name__) #creates flask app object

@app.route("/") #Without hello ("/") if go to the root address (in this case http://127.0.0.1:5000/), this function will be called and it will return the lesson_index.html template.                    #with hello ("/hello"), type /hello after http://127.0.0.1:5000 in the URL.
def index():
    return render_template("lesson_index.html")

@app.route("/about")
def about():
    return render_template("lesson_about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("lesson_portfolio.html")

if __name__ == "__main__": #to se zalaufa samo, če zaženemo direkt ta file. Če ta file importamo in zaženemo nekje drugje, __name__ NI poimenovan __main__ in to preskoči
    app.run(use_reloader=True)