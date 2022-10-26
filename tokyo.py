import requests
import pandas as pd
from bs4 import BeautifulSoup

url='https://www.homemate-research-athletic-field.com/13/list/'

response = requests.get(url)
results = []
other_results_virtual = []
other_results = []
soup = BeautifulSoup(response.text, 'html.parser')
for element in soup.findAll(attrs={'class': 'fa_ttl'}):
    name = element.find('a')
    if name not in results:
        results.append(name.text)
for b in soup.findAll(attrs={'class': 'fa_address'}):
    name2 = b.contents[3]
    other_results_virtual.append(name2.text.strip('\t/\n'))

other_result_length = len(other_results_virtual)

for i in range(0, other_result_length):
    if i % 2 == 0:
        other_results.append(other_results_virtual[i])


df = pd.DataFrame({'Names': results, 'Address': other_results})
df.to_csv('tokyo_tracks.csv', index=False, encoding='utf-8')
