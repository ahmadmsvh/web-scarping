import requests
import html5lib
from bs4 import BeautifulSoup
import time
import pandas as pd

url ='https://www.udemy.com/course/pythonforbeginners/?javascript%3As.js%3A78='

def course_desc():
   resp = requests.get(url,'html5lib')

   bs = BeautifulSoup(resp.text, 'html5lib')
   divs = bs.findAll('div')

   for i in divs:
      print(i)


course_desc()