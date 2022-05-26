import requests
from bs4 import BeautifulSoup
import html5lib.treeadapters.sax
import lxml

# url = 'https://www.daneshjooyar.com/category/mobile-programming/'
url = 'https://www.daneshjooyar.com/category/windows-programming/'
# url = 'https://www.daneshjooyar.com/category/artificialintelligence/'

response = requests.get(url)

bs = BeautifulSoup(response.text, 'html5lib')
page_numbers_ul = bs.select('ul.page-numbers')

tags = page_numbers_ul[0].findAll('li')
last_page_tag = tags[len(tags) - 2]
number = last_page_tag.find('a').text
number_of_pages = int(number)

titles = []
urls = []
for page in range(1, number_of_pages + 1):
   # for page in range(1, 2):
   response = requests.get(url, params={'page': '{}'.format(page)})
   bs = BeautifulSoup(response.text, 'html5lib')

   courses = bs.select('div.course-area')
   courses = courses[0].select('div.course-filter-list')
   courses = courses[0].findAll('a')

   for a_tag in courses:
      title = a_tag.select('h2')[0].text
      titles.append(title)
      urls.append(a_tag['href'])

my_doc = '''<html lang="en" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="bootstrap-grid.min.css">
    <link rel="stylesheet" href="spiral.css">
    <title>Document</title>
    <style>
      a{
      text-decoration: none;
      color: black
      }
    </style>
</head>

<body>'''
for i in range(len(urls)):
   my_doc += '<a href={}> <h2>{}</h2></a> \n'.format(urls[i], titles[i])
my_doc += '</body>'
with open('./files/index.html', 'w') as f:
   f.write(my_doc)