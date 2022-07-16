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

# to be continue
def func07():
  s = """my number is 234 ,0. 
  my frinds number is 789
  """
  compile_regex = re.compile('[a-e]')
  match = compile_regex.findall(s)

  print(match)
# ------------------main---------------------

func06()
