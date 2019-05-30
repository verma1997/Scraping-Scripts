import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re
import schedule

html = urlopen("https://www.cleartrip.com/offers/india")

page_soup = BeautifulSoup(html, "html.parser")

containers = page_soup.findAll("div",{"class":"views-row"})

offers = []
links = []
description = []
expire_duration = []

containers_len = len(containers)

filename = "cleartrip_offers.csv"
headers = "Offers,Links,Description,Expiry Duration,\n"

for contain in containers:
    offer_name_link = contain.find_all("div",{"class":"views-field views-field-title"})
    for names in offer_name_link:
        offers.append(names.text.replace(",",""))
        links.append("https://www.cleartrip.com" + names.a['href'])

    offer_description = contain.find_all("div",{"class":"views-field views-field-field-description"})
    for description_name in offer_description:
        description.append(description_name.text.replace(",","")) 


expire_div = []
expire_div_location = []

for i in range(0,containers_len):
    expire_div.append(containers[i].find("div",{"class":"views-field views-field-field-expiration-date"}))

for i in range(0,containers_len):
    if expire_div[i]!=None:
        expire_div_location.append(i)
    else:
        expire_div_location.append('None')

# expire_span1 = []
for i in expire_div_location:
    if i=='None':
        expire_duration.append('None')
    else:
        expire_duration.append(expire_div[i].find("span",{"class":"field-content"}).text.replace(",",""))

f = open(filename, "a")
f.write(headers)

for i in range(0,containers_len):
    f.write(offers[i] + "," + links[i] + "," + description[i] + "," + expire_duration[i] + "\n")

f.close()
