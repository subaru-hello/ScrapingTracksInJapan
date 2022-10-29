import requests

url = "https://oxylabs.io/blog"

response = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)
