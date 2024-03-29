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

# html = urlopen("https://www.sastiticket.com/offers")
# url = "https://www.sastiticket.com/offers"
urls = [
	"https://www.sastiticket.com/offers/new/",
	"https://www.sastiticket.com/offers/weekend/",
	"https://www.sastiticket.com/offers/mobikwik_new/",
	"https://www.sastiticket.com/offers/bhim/",
	"https://www.sastiticket.com/offers/rupay/"
]

for i in range(0,len(urls)-1):
	html = requests.get(urls[i], get_header())

	page_soup = BeautifulSoup(html.text, "html.parser")

	containers = page_soup.findAll("div",{"class":"col-lg-12 col-md-12 col-xs-12 col-sm-12"})

	for j in containers:
		temp = j.findAll("ul")
		print(temp)

# def job(url):
# 	html = requests.get(url, get_header())

# 	page_soup = BeautifulSoup(html.text, "html.parser")

# 	offer = []
# 	offer_period = []
# 	offer_category = []
# 	offer_description = []

# 	containers = page_soup.find("div",{"class":"col-lg-12 col-md-12 col-xs-12 col-sm-12"})

# 	print(containers)



# schedule.every(1).minutes.do(job)
# schedule.every().day.at("18:43").do(job)
# schedule.every().hour.do(job)
# schedule.every().seconds.do(job)

# while True:
# 	schedule.run_pending()
# 	time.sleep(1)

