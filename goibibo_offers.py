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

url = "https://www.goibibo.com/offers/"

html = requests.get(url, get_header())
    
#building Connection
# html = urlopen("https://www.goibibo.com/offers/")
page_soup = BeautifulSoup(html.text, "html.parser")

#Dumping data inside variable
container = page_soup.findAll("div",{"class":"bot-section"})
promo_container = page_soup.findAll("div",{"class":"back-content"})

#Common Length variable
total = len(container)

#Declaring lists
offers = []
promos = []
links = []
terms_conditions = []

#For Offer Names
for offer_names in container:
	offers.append(offer_names.p.text.replace(",","")) 

#For Links, Promocodes, Terms&Conditions
for content in promo_container:
	
	link_text = content.a['href']
	links.append("https://www.goibibo.com"+link_text)
	
	promo_content = content.find_all("div",{"class":"back-content-top-inner"})
	conditions = content.find_all("div",{"class":"tnc-section"})
	
	for terms in conditions:
		terms_conditions.append(terms.li.text.replace(",",""))
		# print(terms.li.text)

	for promo in promo_content:
		promo_code = promo.find_all("div",{"class":"promocode"})
		for promo_text in promo_code:
			promos.append(promo_text.text)
			# print(promo_text.text)

#Opening csv file to store data
filename = "goibibo_offers.csv"
f = open(filename,"a")
headers = "Offer Name,Link,Promocode,Description,Booking Channel \n"
f.write(headers)	

for i in range(0,total):
	f.write(offers[i] + "," + links[0] + "," + promos[i] + "," + terms_conditions[i] + "\n")

f.close()

#Scheduler

# schedule.every(1).minutes.do(job)
# schedule.every().day.at("18:43").do(job)
# schedule.every().hour.do(job)
# schedule.every().seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
