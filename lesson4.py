import json
with open("opportunities.json","r") as file:
    opportunities=json.load(file)

for opportunity in opportunities:
    print(opportunity["title"],opportunity["location"])
    