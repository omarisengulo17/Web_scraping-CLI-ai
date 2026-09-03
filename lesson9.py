import json
from trace import Trace
with open("all.json","r") as file:
    unique_jobs=json.load(file)
    keyword = input("Enter job keyword: ")
    keyword = keyword.lower()
    found = False
for job in unique_jobs:
    if keyword in job["title"].lower():
     found=True
     print(job["title"],job["location"])

if found == False:
     print("No jobs found")