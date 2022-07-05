import pandas as pd
import numpy as np
import openpyxl
import requests
import xlsxwriter
from bs4 import BeautifulSoup
# **
import urllib.parse


def func01():
    url = 'https://www.db-book.com/slides-dir/PDF-dir/ch2.pdf'
    response = requests.get(url,stream=True)

    with open('./PDF/ch2.pdf','wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def func02():
    url = 'https://programmershouse.ir/Syllabus/Files/SQL Server 2.pdf#divPopupViewPDFDialog'
    response = requests.get(url, stream=True)

    with open('./PDF/SQL_Server_2.pdf', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def func03():
    str = 'hello+world+Paython'

    print(urllib.parse.unquote(str))


def func04():

    str = 'hello+world+Paython'

    print(urllib.parse.unquote_plus(str))



def func05():

    str = 'Hello%20World%0A'

    print(urllib.parse.unquote(str))


def func06():
    str = 'Hello World Python'

    print(urllib.parse.quote(str))


def func07():
    str = 'Hello World Python'

    encode = urllib.parse.quote(str)
    print(encode)
    print(urllib.parse.unquote(encode))


# To be Continue
def func08():
    url = 'https://dyysg.org.uk/docs.php'
    response = requests.get(url)

    bs = BeautifulSoup(response.text,'lxml')
    a_tags = bs.findAll('a')



    for a_url in a_tags:
        try:
            if 'pdf' in a_url['href']:
                print(a_url['href'])
        except:
            pass

# ------------------main---------------------

func08()