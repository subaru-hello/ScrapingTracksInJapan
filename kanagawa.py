import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.homemate-research-athletic-field.com/14/list/"

response = requests.get(url)
track_names = []
track_address_virtual = []
track_address = []
soup = BeautifulSoup(response.text, "html.parser")

for element in soup.findAll(attrs={"class": "fa_ttl"}):
    name = element.find("a")
    if name not in track_names:
        track_names.append(name.text)
for b in soup.findAll(attrs={"class": "fa_address"}):
    name2 = b.contents[3]
    track_address_virtual.append(name2.text.strip("\t/\n"))

track_address_length = len(track_address_virtual)

for i in range(0, track_address_length):
    if i % 2 == 0:
        track_address.append(track_address_virtual[i])

prefecture = ["kanagawa"] * len(track_address)

df = pd.DataFrame(
    {"Names": track_names, "Address": track_address, "Prefecture": prefecture}
)
df.to_csv("./csvs/kanagawa_tracks.csv", index=False, encoding="utf-8")
