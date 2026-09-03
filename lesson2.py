import requests
from bs4 import BeautifulSoup

response=(requests.get("https://example.com"))
print(response.status_code)
soup =BeautifulSoup(response.text,"html.parser")
print(soup.select_one("title").text)
print(soup.select_one("a").text)
print(soup.select_one("a").get("href"))