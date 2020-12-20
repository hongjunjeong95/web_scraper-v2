from scrapperSO import get_SOJobs
from scrapperWWR import get_WWRJobs
from scrapperRemote import get_WWRJobs

SO = get_SOJobs("python")
WWR = get_WWRJobs("python")
RemoteJobs = get_RemoteJobs("python")
jobs = SO + WWR + RemoteJobs

print(jobs)