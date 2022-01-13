import requests
from bs4 import BeautifulSoup as bs
from backend.models import split_name
import pandas as pd

letters = ["A", "B"]

parties = []
first_names = []
last_names = []


for page_letter in letters:
  res = requests.get("http://sejm.gov.pl/Sejm9.nsf/poslowie.xsp?type={}".format(page_letter))
  soup = bs(res.content, 'html.parser')

  all_letters = soup.findAll("ul", "deputies")
  for letter in all_letters:
    letter_mps = letter.findAll("li")
    for mp in letter_mps:
      name = mp.find("div", "deputyName").text
      party = mp.find("div", "deputy-box-details").find("strong").text

      first_name, last_name = split_name(name)
      first_names.append(first_name)
      last_names.append(last_name)
      parties.append(party)

      print("Updating information about {} {} {}".format(first_name, last_name, party))

df = pd.DataFrame({'first_name': first_names, 'last_name': last_name, 'party': parties})
print(df)
df.to_csv('mps.csv')
