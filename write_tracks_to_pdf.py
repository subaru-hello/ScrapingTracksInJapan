from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary
import re
import urllib
import pandas as pd
import tabula
import os

base_url = 'https://www.city.kawasaki.jp/nakahara'
driver = webdriver.Chrome()
driver.get("https://www.city.kawasaki.jp/nakahara/page/0000088519.html")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")


save_dir = 'track_pdfs'
if save_dir not in os.listdir("./"):
    os.mkdir(save_dir)

for element in soup.findAll(attrs={"class": "mol_attachfileblock"}):
    name = element.find("a")
    pdf_relative_path = name.get('href')
    pdf_path = re.sub(r'^.', base_url, pdf_relative_path)
    file_name = pdf_relative_path.split("/")[-1]
    urllib.request.urlretrieve(pdf_path, os.path.join(save_dir, file_name))


# df = tabula.read_pdf(pdf_file_name, pages = '1', multiple_tables = False)[0]
#print(pdf_path)


# base url
# https://www.city.kawasaki.jp/nakahara/
driver.quit
