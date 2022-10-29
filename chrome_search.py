from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get("https://www.city.kawasaki.jp/nakahara/page/0000088519.html")

results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
for element in soup.findAll(attrs={"class": "mol_attachfileblock"}):
    name = element.find("a")
    print(name)

driver.quit
