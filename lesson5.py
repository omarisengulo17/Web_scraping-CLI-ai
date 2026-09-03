opportunities_data = [
    {
        "title": "Python Developer",
        "organization": "Tech Tanzania"
    },
    {
        "title": "Python Developer",
        "organization": "Tech Tanzania"
    },
    {
        "title": "Flutter Developer",
        "organization": "Mobile Africa"
    },
    {
        "title": "ominja khan",
        "organization": "muhindi"
    }
]

seen = set()
unique_opportunities = []

for opportunity in opportunities_data:

    key = opportunity["title"] + "|" + opportunity["organization"]

    if key in seen:
        continue

    seen.add(key)
    unique_opportunities.append(opportunity)

print(unique_opportunities)