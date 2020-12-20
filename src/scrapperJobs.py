from scrapperSO import get_SOJobs
from scrapperWWR import get_WWRJobs
from scrapperRemote import get_RemoteJobs

def get_jobs(word):
  SO = get_SOJobs(word)
  WWR = get_WWRJobs(word)
  RemoteJobs = get_RemoteJobs(word)
  jobs = SO + WWR + RemoteJobs
  return jobs