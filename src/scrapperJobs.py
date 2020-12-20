from scrapperSO import get_SOJobs
from scrapperWWR import get_WWRJobs

SO = get_SOJobs("python")
WWR = get_WWRJobs("python")
jobs = SO+WWR
print(jobs)