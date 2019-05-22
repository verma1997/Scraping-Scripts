import requests
from urllib.request import urlopen
# import urllib2
import time
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re
import schedule
# import json

html = urlopen("https://www.cleartrip.com/offers/india")

page_soup = BeautifulSoup(html, "html.parser")

filename = "cleartrip_offers.csv"

containers_div = page_soup.findAll("div",{"class":"field-content"})
containers_span = page_soup.findAll("span",{"class":"field-content"})

print(len(containers_div))
print(len(containers_span))