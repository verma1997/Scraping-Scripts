import schedule
import time
from datetime import datetime

a = "Priyanshu"

def job():
	print(a)

schedule.every(1).minutes.do(job)
# schedule.every().day.at("10:50").do(job)
# schedule.every().hour.do(job)
# schedule.every().seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(5)