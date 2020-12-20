from flask import Flask, render_template, redirect, request
from scrapperJobs import get_jobs
from exporter import save_to_file

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

@app.route('/export')
def export():
  try:
    word = request.args.get('word')
    if not word:
      print("not word")
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      print("not jobs")
      raise Exception()

    save_to_file(jobs, word)
    return redirect("/")
  except IOError:
    print("error")
    return redirect("/")

app.run(host="127.0.0.1")