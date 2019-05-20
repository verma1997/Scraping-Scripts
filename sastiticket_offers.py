import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re
import schedule

html = urlopen("https://www.sastiticket.com/offers")

page_soup = BeautifulSoup(html, "html.parser")

offers = []

containers = page_soup.findAll("div",{"class":"col-lg-3 col-md-3 col-xs-12 col-sm-12"})

image_links = page_soup.findAll("img",{"class":"img-responsive"})

container_len = len(containers)

filename = "sastiticket_offers.csv"

def job():
	f = open(filename,"a")
	
	for link in image_links:
		# print(i['src'],i.get_text())
		f.write(link['src'].link.get_text())

	for links in containers:
		a = links.find('a')
		print(a['href'],a.get_text())



# print(len(image_links))

