import requests
from bs4 import BeautifulSoup

def extract_job(html):
  # title, company, location, link
  job_info_link = html.find_all('a')
  
  if len(job_info_link) > 1:
    job_info_link = job_info_link[1]
  else:
    job_info_link = job_info_link[0]
  
  link = f"https://weworkremotely.com/{job_info_link['href']}"
  job_info = job_info_link.find_all("span")
  company = job_info[0].get_text()
  title = job_info[1].get_text()
  location = job_info[5].get_text()

  return {
    "title" : title,
    "link" : link,
    "company" : company,
    "location" : location
  }

def extract_jobs(url):
  jobs=[]
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("section",{"class":"jobs"}).find("ul").find_all("li",{"class":"feature"})
  for result in results:
    job = extract_job(result)
    print(job)
    jobs.append(job)
  return jobs

def get_WWRJobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = extract_jobs(url)
  return jobs