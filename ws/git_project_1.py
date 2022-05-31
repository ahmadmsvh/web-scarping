import requests
from bs4 import BeautifulSoup
import pandas as pd

def make_file():
   url = 'https://github.com/topics'

   response = requests.get(url).text
   print(len(response))

   with open('./files/git_1.html', 'w') as f:
      f.write(response)

def get_topic():
   url = 'https://github.com/topics'

   response = requests.get(url).text

   bs = BeautifulSoup(response, 'html5lib')
   topics = bs.findAll('p',{'class':'f3 lh-condensed mb-0 mt-1 Link--primary'})

   topics_list=[]
   for topic in topics:
      topics_list.append(topic.text.strip())
   print(topics_list)

def get_descr():
   url = 'https://github.com/topics'

   response = requests.get(url).text

   bs = BeautifulSoup(response, 'html5lib')
   descrs = bs.findAll('p',{'class':'f5 color-fg-muted mb-0 mt-1'})

   descr_list = []

   for descr in descrs:
      descr_list.append(descr.text.strip())

   for descr in descrs:
      print(descr.text.strip())

#------------------------------------
get_descr()