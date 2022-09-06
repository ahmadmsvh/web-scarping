import requests
import pickle
import schedule
import time


def readTitle():
   url = "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&pageSize=20&pageNo=1"

   payload={}
   headers = {}

   response = requests.request("GET", url, headers=headers, data=payload)
   jsn = response.json()

   title = jsn['data']['catalogs'][1]['articles'][0]['title']

   date = jsn['data']['catalogs'][1]['articles'][0]['releaseDate']

   from datetime import datetime

   date = datetime.fromtimestamp(date/1000)
   date = str(date)[:19]
   # print(date)

   try:
      with open('./binance/binance_title.bin', 'rb') as fp:
         title_old_1 = ''
         title_old = True
         while title_old:
            try:
               title_old = pickle.load(fp)
               print(title_old)
               title_old_1 = title_old
            except:
               title_old = False
   except Exception as e:
      print(e)

   try:
      with open('./binance/binance_title.bin', 'ab') as fp:
         title += (" - "+date)
         if title != title_old_1:

            pickle.dump(title, fp)
   except Exception as e:
      print(e)

schedule.every(5).seconds.do(readTitle)

while True:
   schedule.run_pending()
   time.sleep(5)
   print('\n')