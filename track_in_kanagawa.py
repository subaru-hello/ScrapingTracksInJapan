import requests
url='https://www.homemate-research-athletic-field.com/14/list/'

from bs4 import BeautifulSoup

response = requests.get(url)
results = []
soup = BeautifulSoup(response.text, 'html.parser')
for element in soup.findAll(attrs={'class': 'fa_ttl'}):
    name = element.find('a')
    results.append(name.text)

for el in soup.findAll(attrs={'class': 'fa_address'}):
    address = el.find('span')
    results.append(address.text)



print(results)