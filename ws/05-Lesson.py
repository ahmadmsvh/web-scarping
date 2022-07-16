from typing import re

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


def func08():
    url = 'https://dyysg.org.uk/docs.php'
    response = requests.get(url)
    bs = BeautifulSoup(response.text,'lxml')
    a_tags = bs.findAll('a')
    for a_url in a_tags:
        try:
            if 'pdf' in a_url['href']:
                pdfUrl= ''
                if 'https' not in a_url['href']:
                    pdfUrl = 'https://dyysg.org.uk'+a_url['href']
                else:
                    pdfUrl=a_url['href']

                pdfResponse = requests.get(pdfUrl)
                response_pdf_url = pdfResponse.url

                unquote_pdf_url= urllib.parse.unquote(response_pdf_url)
                split_pdf_url = unquote_pdf_url.split('/')
                file_name = split_pdf_url[-1]
                file_name = file_name.replace(' ','_')

                with open('./PDF/'+file_name,'wb') as f:
                    f.write(pdfResponse.content)

        except:
            pass


def func09():
    url = 'https://programmershouse.ir/Home/Short-Term.aspx?page='
    title_list_PRG = []
    precondition_list_PRG = []

    title_list_DB = []
    precondition_list_DB = []

    title_list_PO = []
    precondition_list_PO = []

    writer = pd.ExcelWriter('./XLSX/07-Programmershouse-Short-Term.xlsx', engine='xlsxwriter')

    # ==============================================================================================
    for page in range(1,5):
        response = requests.get(url+str(page))
        bs = BeautifulSoup(response.text,'lxml')
        for title in bs.select('#div-PCourses-PRG td.ItemTitle.EnglishControlsBold.LeftAlignControl'):
            title_list_PRG.append(title.text.strip())

        for precondition in bs.select('#div-PCourses-PRG td.EnglishControls.LeftAlignControl'):
            precondition_list_PRG.append(precondition.text.strip())

    dict =\
        {
            'Title':title_list_PRG,
            'Precondition':precondition_list_PRG
        }
    data = pd.DataFrame(dict)

    data.to_excel(writer, sheet_name='برنامه نویسی', index=False)

    # ==============================================================================================
    for page in range(1, 2):
        response = requests.get(url + str(page))
        bs = BeautifulSoup(response.text, 'lxml')
        for title in bs.select('#div-PCourses-DB td.ItemTitle.EnglishControlsBold.LeftAlignControl'):
            title_list_DB.append(title.text.strip())

        for precondition in bs.select('#div-PCourses-DB td.EnglishControls.LeftAlignControl'):
            precondition_list_DB.append(precondition.text.strip())

    dict = \
        {
            'Title': title_list_DB,
            'Precondition': precondition_list_DB
        }
    data = pd.DataFrame(dict)
    data.to_excel(writer, sheet_name='دیتابیس', index=False)

    # ==============================================================================================
    for page in range(1, 2):
        response = requests.get(url + str(page))
        bs = BeautifulSoup(response.text, 'lxml')
        for title in bs.select('#div-PCourses-PO td.ItemTitle.EnglishControlsBold.LeftAlignControl'):
            title_list_PO.append(title.text.strip())

        for precondition in bs.select('#div-PCourses-PO td.EnglishControls.LeftAlignControl'):
            precondition_list_PO.append(precondition.text.strip())

    dict = \
        {
            'Title': title_list_PO,
            'Precondition': precondition_list_PO
        }
    data = pd.DataFrame(dict)
    data.to_excel(writer, sheet_name='متدولوژی', index=False)

    writer.save()


# ------------------main---------------------

func09()