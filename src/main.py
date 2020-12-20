from flask import Flask, render_template, redirect, request
from scrapperJobs import get_jobs

app = Flask("Job Scrapper", template_folder="./src/templates")
db={}

@app.route('/')
def index():
  try:
    return render_template("home.html")
  except IOError:
    return redirect("/")

@app.route('/search')
def search():
  try:
    word = request.args.get('term')
    if word:
      word = word.lower()
      if word in db:
        jobs = db[word]
      else:
        jobs = get_jobs(word)
        db[word]=jobs
    else:
      redirect("/")
    return render_template("search.html", resultsNumber=len(jobs),searchingBy=word, jobs=jobs)
  except IOError:
    return redirect("/")

app.run(host="127.0.0.1")