from flask import Flask, render_template, redirect

app = Flask("Job Scrapper", template_folder="./src/templates")


@app.route('/')
def index():
    try:
        return render_template("home.html")
    except IOError:
        return redirect("/")

app.run(host="127.0.0.1")