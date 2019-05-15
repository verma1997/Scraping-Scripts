# Libraries used.
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
from datetime import datetime
import schedule

# Funtion to perform job.
def job():
    """
    Scrape <a> links from https://www.rhfleet.org/
    
    """
    html = urlopen("https://www.makemytrip.com/")
    bsObj = BeautifulSoup(html, 'lxml')                
    
    links = []
    for link in bsObj.findAll('a'):
        links.append(link.get('href'))

    """
    print 50th index link with timestamp.
    """
    print(links[50], str(datetime.now()))

"""
Scheduler:
For example: it will return the output after every 6 second.
We can set it for 24 hours with the help of which our database will
be updated every 24 hours. 
"""
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("21:39").do(job)
schedule.every(6).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
