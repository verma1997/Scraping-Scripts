from random import choice
import requests
import urllib.request
from bs4 import BeautifulSoup
import io

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

url = "https://www.goindigo.in/campaigns/indigo-offers.html"

html = requests.get(url, headers=get_header())

soup = BeautifulSoup(html.text, 'html.parser')

def job():
    container = soup.findAll("div",{"class":"commonBottomAdon"})

    total = len(container)

    offer_links = []
    offer_image = []
    offer_name = []
    offer_description = []

    for i in container:
        links = i.find("a")
        offer_links.append(links['href'])

        image = i.find("img")
        offer_image.append("https://www.goindigo.in" + image['src'])

        name = i.find("h6")
        offer_name.append(name.text.replace(",",""))

        description = i.find("p")
        offer_description.append(description.text.replace(",",""))

    filename = "indigo_offers.csv"
    f = open(filename,"a",encoding="utf-8")
    headers = "Offer Name,Link,Description,Image Link,Booking Channel \n"
    f.write(headers)    

    for i in range(0,total):
        f.write(offer_name[i] + "," + offer_links[0] + "," + offer_description[i] + "," + offer_image[i] + "\n")

    f.close()


# Scheduler

# schedule.every().hour.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)



