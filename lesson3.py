from bs4 import BeautifulSoup
import json

html = """
<div class="opportunity">
    <h2>   Python Developer</h2>
    <p class="organization">    Tech Tanzania</p>
    <p class="location">   Dar es Salaam</p>
     <a href="https://example.com/python">Apply Now</a>
</div>

<div class="opportunity">
    <h2>   Flutter Developer</h2>
    <p class="organization">    Mobile Africa</p>
    <p class="location">   Arusha</p>
    <a href="https://example.com/flutter">Apply Now</a>
</div>

<div class="opportunity">
    <h2>    Data Analyst</h2>
    <p class="organization">    Tanzania Data Lab</p>
    <p class="location">   Dodoma</p>
    <a href="https://example.com/data">Apply Now</a>
</div>
"""


soup =BeautifulSoup(html,"html.parser")
soup.find(".opportunity")

opportunities = soup.select(".opportunity")
opportunities_data = []

for opportunity in opportunities:
   

    location_element = opportunity.select_one(".location")

    if location_element:
        location = location_element.text.strip()
    else:
        location = "Not provided"

    opportunity_data = {
        "title": opportunity.select_one("h2").text.strip(),
        "organization": opportunity.select_one(".organization").text.strip(),
        "location": location,
        "url": opportunity.select_one("a").get("href")
    }
        
    opportunities_data.append(opportunity_data)
print(opportunities_data)

with open("opportunities.json","w") as file:
    opportunities=json.dump(opportunities_data,file)