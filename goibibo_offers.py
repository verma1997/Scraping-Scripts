import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re
import schedule

html = urlopen("https://www.goibibo.com/offers/")

page_soup = BeautifulSoup(html, "html.parser")

container = page_soup.findAll("div",{"class":"bot-section"})

promo_container = page_soup.findAll("div",{"class":"back-content"})

total = len(container)


offers = []
promos = []
links = []
terms_conditions = []

for offer_names in container:
	offers.append(offer_names.p.text.replace(",","")) 

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

filename = "goibibo_offers.csv"
f = open(filename,"a")
headers = "Offer Name,Link,Promocode,Terms & Condition,Booking Channel \n"
f.write(headers)	

for i in range(0,total):
	f.write(offers[i] + "," + links[0] + "," + promos[i] + "," + terms_conditions[i] + "\n")

f.close()

# schedule.every(1).minutes.do(job)
# schedule.every().day.at("18:43").do(job)
# schedule.every().hour.do(job)
# schedule.every().seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
