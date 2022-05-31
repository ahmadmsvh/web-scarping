import requests
import html5lib
from bs4 import BeautifulSoup
import time
import pandas as pd

url ='https://www.binance.com/en/news'
hrefs = []

def read_last_news(old_news):
   resp = requests.get(url, 'html5lib')

   bs = BeautifulSoup(resp.text, 'html5lib')
   news_href = bs.select('div.css-1i9bvdl')[0].select('a')[0]['href']
   if news_href != old_news:
      old_news = news_href
      hrefs.append(old_news)
   return old_news

last_news = ''
while 1:
   last_news = read_last_news(last_news)
   print(hrefs)
   time.sleep(3)