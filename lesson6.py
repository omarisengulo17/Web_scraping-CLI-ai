import requests
from bs4 import BeautifulSoup

def scrape_page():
 response=(requests.get("https://example.com"))

 soup=BeautifulSoup(response.text,"html.parser")
 return(soup.select_one("title").text)

title = scrape_page()
print(title)