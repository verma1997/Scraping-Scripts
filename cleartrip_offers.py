from random import choice
import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re
import schedule

headers = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Googlebot/2.1 (+http://www.google.com/bot.html)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36',
    'Gigabot/3.0 (http://www.gigablast.com/spider.html)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/533.3 '
    '(KHTML, like Gecko)  QtWeb Internet Browser/3.7 http://www.QtWeb.net',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, '
    'like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4pre) '
    'Gecko/20070404 K-Ninja/2.1.3',
    'Mozilla/5.0 (Future Star Technologies Corp.; Star-Blade OS; x86_64; U; '
    'en-US) iNet Browser 4.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) '
    'Gecko/20080414 Firefox/2.0.0.13 Pogo/2.0.0.13.6866',
    'WorldWideweb (NEXT)'
]

def get_header():
    return {'User-Agent':choice(headers)}

url = "https://www.cleartrip.com/offers/india"

html = requests.get(url, get_header())

# html = urlopen("https://www.cleartrip.com/offers/india")

page_soup = BeautifulSoup(html.text, "html.parser")

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
