import requests
from bs4 import BeautifulSoup
from datetime import datetime 
import time

# from keep_alive import keep_alive
# import pytz

# keep_alive()
while(True):

    # tz_NY = pytz.timezone('Asia/Kolkata')
    # datetime_NY = datetime.now(tz_NY)
    now = datetime.now()
      
    # current_time = datetime_NY.strftime("%H:%M:%S - (%d/%m)")
    current_time = now.strftime("%H:%M:%S")
    print(f'At time : {current_time} IST')
  
    response = requests.get('https://finance.yahoo.com/cryptocurrencies/')
    text = response.text
    html_data = BeautifulSoup(text, 'html.parser')
    headings = html_data.find_all('tr')[0]
    headings_list = []
    for x in headings:
        headings_list.append(x.text)
    headings_list = headings_list[:10]
  
    data = []
  
    for x in range(1, 6):
        row = html_data.find_all('tr')[x]
        column_value = row.find_all('td')
        dict = {}
          
        for i in range(10):
            dict[headings_list[i]] = column_value[i].text
        data.append(dict)
          
    for coin in data:
        print(coin)
        print('')
    time.sleep(100)


