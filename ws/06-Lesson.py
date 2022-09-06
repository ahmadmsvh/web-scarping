import pandas as pd
import numpy as np
import openpyxl
import requests
import xlsxwriter
from bs4 import BeautifulSoup
import urllib.parse

# *
import re
from re import split


# https://pythex.org/


def func01():
  s = 'programmershous:a computer sience portal for students'
  match = re.search(r'portal',s)

  print(match.start())
  print(match.end())


def func02():
  s = 'programmershous.ir'
  match = re.search(r'.',s)

  print(match)


def func03():
  s = 'programmershous.ir'
  match = re.search(r'\.',s)

  print(match)

def func04():
  s = """my number is 234 ,0. 
  my frinds number is 789
  """
  regex = '\d+'
  match = re.findall(regex,s)

  print(match)


def func05():
  s = """my number is 234 ,0. 
  my frinds number is 789
  """
  regex = '\d*'
  match = re.findall(regex,s)

  print(match)


def func06():
  s = """my number is 234 ,0. 
  my frinds number is 789
  """
  compile_regex = re.compile('[a-e]')
  match = compile_regex.findall(s)

  print(match)


def func07():

  compile_regex = re.compile('ab*')
  match = compile_regex.findall('ababbaabbb')
  print(match)


def func08():
  print(split('\W+','Worlds, worlds , Worlds'))#[Worlds,worlds,Worlds]

  print(split('\W+',"World's worlds Worlds"))#[World,s,worlds,Worlds]

  print(split('\W+',"on 15th jan 2019, at 12:46 AM"))

  print(split('\d+',"on 15th jan 2019, at 12:46 AM"))


def func09():
  print(re.split('\d+', "on 15th jan 2019, at 12:46 AM"))

  print(re.split('\d+', "on 15th jan 2019, at 12:46 AM",1))

  print(re.split('\d+', "on 15th jan 2019, at 12:46 AM",2))

  print(re.split('[a-f]+', "Aey, Boy oh boy, come here"))

  print(re.split('[a-f]+', "Aey, Boy oh boy, come here",flags=re.IGNORECASE))

def func10():
  s = "welcome to programmers house"
  re_search = re.search(r"\bpro",s)

  print(re_search.start())
  print(re_search.end())
  print(re_search.span())

def func11():
  url = 'https://quotes.toscrape.com/'
  response = requests.get(url)
  data = BeautifulSoup(response.content,"html5lib")

  tags = data.findAll(['a','div'])

  for tag in tags:
    print(tag)
    print("-------------------------------------------------")

  print("re")
  re_tags = data.findAll(re.compile('^a|^div'))

  for tag in re_tags:
    print(tag)
    print("-------------------------------------------------")


def func12():
  url = 'https://quotes.toscrape.com/'
  response = requests.get(url)
  data = BeautifulSoup(response.content, "html5lib")

  tags = data.findAll('div',attrs={'class':'quote'})

  print(len(tags))
  for tag in tags:
    print(tag.text)
    print("-------------------------------------------------")


  print("re")
  re_tags = data.findAll('div',re.compile('^quote'))
  print(len(re_tags))
  for tag in re_tags:
    print(tag.text)
    print("-------------------------------------------------")


def func13():
  with open('./HTML/scrape.html','r') as f:
  # response = requests.get('http://localhost:63342/WebScraping/HTML/scrape.html?_ijt=5as08thmgi7jirbm2josh9nohf&_ij_reload=RELOAD_ON_SAVE')
    response = f.read()
    data = BeautifulSoup(response,'lxml')
    tr_tags = data.findAll('tr')

    emails =[]
    phones =[]
    for tr in tr_tags:
      td_tags = tr.findAll('td')
      if len(td_tags) != 0:
        emails.append(td_tags[1].text.strip())
        phones.append(td_tags[2].text.strip())

    print(emails)
    print(phones)


def func14():
    # url = 'https://www.progolftour.de/contact'
    # url = 'https://bramptongolf.com/contact/'
    # url = 'https://programmershouse.ir/ContactUS/AboutUs.aspx?tid=Opinions'
    # url = 'https://www.rubyhill.com/club-contacts'
    url = 'https://www.tatumranchgc.com/club-contacts'

    data = requests.get(url)

    # re_emails = re.findall(r'(\b[\w\.-]+@[\w]+\.[A-Za-z][A-Za-z]+\b)', data.text)
    re_emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
    re_phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)


    for email in re_emails:
      print(email)

    for phone in re_phones:
      print(phone)

    print("======================================re================================================")


def func15():
  with open('./files/scrape.html', 'r') as f:
    # response = requests.get('http://localhost:63342/ws/files/scrape.html?_ijt=pe8gn7doh88ijnukc4fgt88skn&_ij_reload=RELOAD_ON_SAVE')
    response = f.read()
    data = BeautifulSoup(response, 'lxml')
    regex = re.compile('.*@.*\.\w{2,4}')
    a = regex.findall(data.text)
    print(a)
    regex = re.compile('\d-\d{3}-\d{3}-\d{4}')
    b = regex.findall(data.text)
    print(b)

    print("======================================re================================================")

if __name__ == '__main__':

  func14()

