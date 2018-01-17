'''import requests, bs4

response = requests.get('https://en.wikipedia.org/wiki/A.J.W._McNeilly')
html=response.text
soup=bs4.beautifulSoup(html, "html.parser")
soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a.get('href')
'''

import datetime

start_time = '3/31/2016 22:57:12'
time_stamp = datetime.datetime.strptime(start_time, "%m/%d/%Y %H:%M:%S")

day_of_week = time_stamp.strftime('%A')
month = time_stamp.month
hour = time_stamp.hour

print ('output: ',time_stamp,month, hour, day_of_week)