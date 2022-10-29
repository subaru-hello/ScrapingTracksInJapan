import requests
import pandas as pd
from bs4 import BeautifulSoup

# 10から15までループさせる

url = "https://www.homemate-research-athletic-field.com/14/list/"

response = requests.get(url)
# track_name
track_names = []

# track address
track_address_virtual = []
track_address = []

# track entrance_fee
entrance_fee = []

# available times
open_times = []

# hurdles is available?
hurdle_available = []

# name and address
soup = BeautifulSoup(response.text, "html.parser")
for element in soup.findAll(attrs={"class": "fa_ttl"}):
    name = element.find("a")
    if name not in results:
        track_names.append(name.text)
for b in soup.findAll(attrs={"class": "fa_address"}):
    name2 = b.contents[3]
    track_address_virtual.append(name2.text.strip("\t/\n"))

other_result_length = len(track_address_virtual)

for i in range(0, other_result_length):
    if i % 2 == 0:
        track_address.append(track_address_virtual[i])

# extract track names and search it with chrome, and push each results to designated arrays.

# open_hour

# entrance_fee

# hurdle available


# output to csv
df = pd.DataFrame(
    {
        "Names": track_names,
        "Address": track_address,
        "OpenHour": open_times,
        "EntranceFee": entrance_fee,
        "HurdleAvailablity": hurdle_available,
    }
)
df.to_csv("results.csv", index=False, encoding="utf-8")
