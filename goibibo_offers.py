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

offers = []

containers = page_soup.findAll("div",{"class":"bot-section"})

container_len = len(containers)

filename = "goibibo_offers.csv"
# headers = "Offers,Time\n"

f = open("goibibo_offers.csv","a");

# f.write(headers)

def job():
	f = open(filename, "a")	
	for item in page_soup.select("[class^='sub-heading click-effects']"):
		print(item.text + str(datetime.now()))
		f.write(item.text + "\t" + str(datetime.now()) + "\n")

	print("\n")
	f.close()


schedule.every(1).minutes.do(job)
# schedule.every().day.at("18:43").do(job)
# schedule.every().hour.do(job)
# schedule.every().seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# url = "https://www.goibibo.com/offers/"
# url = "https://www.sastiticket.com/offers"

#opening up connection and grabing the content
# uClient = uReq(url)

#dumping the content in a variable
# page_html = uClient.read()

# uClient.close()

#html parser
# page_soup = soup(page_html, "html.parser")

# containers = page_soup.findAll("div",{"class":"bot-section"})

# container_len = len(containers)

# filename = "goibibo_offers.csv"
# f = open(filename, "w")

# headers = "Name\n"
# f.write(headers)

# for item in page_soup.select("[class^='sub-heading click-effects']"):
# 	print(item.text)
# 	f.write(item.text + "\n")

# for i in range(0,container_len):
# 	print(containers[i].p["onclick"])
# 	f.write(containers[i].p["onclick"] + "\n")

# f.close()

# page_soup = soup(page_html, "html.parser")
# links = []

# for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
# 	links.append(link.get('href'))

# print(links)
