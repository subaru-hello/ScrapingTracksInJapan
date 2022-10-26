import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get('https://your.url/here?yes=brilliant')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
for element in soup.findAll(attrs={'class': 'title'}):
    name = element.find('a')
    results.append(name.text)