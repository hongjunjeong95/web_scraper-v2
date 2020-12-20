import requests
from bs4 import BeautifulSoup

def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def get_SOJobs(word):
  url = f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_page(url)
  print(last_page)

get_SOJobs("python")