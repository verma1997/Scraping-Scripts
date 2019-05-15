import requests
from urllib.request import urlopen as uReq
import time
from bs4 import BeautifulSoup as soup
import csv
import re

url = "https://en.wikipedia.org/wiki/Hubstaff"

uClient = uReq(url)

html_page = uClient.read()

uClient.close()

page_soup = soup(html_page, "html.parser")

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print (link.get('href'))