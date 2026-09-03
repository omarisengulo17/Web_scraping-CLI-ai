import requests

response=(requests.get("https://google.com"))

print(response.status_code)
print(response.text[0:200])