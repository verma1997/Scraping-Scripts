# Circles - IIMA
Web scraping assignments

## Technologies Used:
1. Python <br/>
  1.1 BeautifulSoup
## Information:

| S.No. | Website       | Storage Format  | Scheduling |
| ----- | ------------- | --------------- | ---------- |
| 1.    | GoIbibo       | CSV             | Done       |
| 2.    | Cleartrip     | CSV             | Done       |
| 3.    | Sastiticket   | CSV             | Done       |
| 4.    | Yatra         | JSON            | Done       |
| 5.    | Ixigo         | CSV             | Done       |
| 6.    | EaseMyTrip    | CSV             | Done       |
| 7.    | Paytm Flights | CSV             | Done       |
| 8.    | Indigo        | CSV             | Done       |
| 9.    | Akbartravels  | CSV             | Done       |

Still in progress
## How it works?
1. `pip install beautifulsoup4`
2. `pip install schedule`

## How to use scheduler:
  ### Task scheduling 
   #### After every 10mins.  
   schedule.every(10).minutes.do(job_name) 

   #### After every hour. 
   schedule.every().hour.do(job_name) 

   #### Every day at 12am or 00:00. 
   schedule.every().day.at("00:00").do(job_name) 

   #### After every 5 to 10mins in between. 
   schedule.every(5).to(10).minutes.do(job_name) 
  
