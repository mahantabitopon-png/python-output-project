import requests

url = "https://www.google.com"
response = requests.get(url)

with open("website.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Website HTML saved successfully as website.html")
