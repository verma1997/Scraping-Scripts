import requests
from urllib.request import urlopen
# import urllib2
import time
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re
import schedule

html = urlopen("https://www.sastiticket.com/offers")

page_soup = BeautifulSoup(html, "html.parser")

offers = []

filename = "sastiticket_offers.csv"

img_links = []
a_links = []

def job():
	containers = page_soup.findAll("div",{"class":"col-lg-3 col-md-3 col-xs-12 col-sm-12"})

	image_links = page_soup.findAll("img",{"class":"img-responsive"})
	
	f = open(filename,"a")

	for links in containers:
		a = links.find('a')
		a_links = a['href']
		print(a_links)
		f.write(a_links + "\n")
	
	f.write("\n")
		
	for link in image_links:
		img_links = link['src']
		print(img_links)
		f.write(img_links + "\n")

	f.close()

schedule.every(1).minutes.do(job)
schedule.every().day.at("18:43").do(job)
schedule.every().hour.do(job)
schedule.every().seconds.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)


