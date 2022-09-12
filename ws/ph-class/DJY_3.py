import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.daneshjooyar.com/'

response = requests.get(url)
bs = BeautifulSoup(response.text, 'html5lib')
categories_tag = bs.select('div.catlist')

cat_urls = categories_tag[0].findAll('a')
categories = []
result = []
i = 0
for a in cat_urls:
   categories.append([a.text.strip(), a['href']])
   # print(a.text.strip())
for cat in categories:
   url = 'https://www.daneshjooyar.com/'+cat[1]
   cat_name = cat[1].split('/')[2]

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
      response = requests.get(url, params={'page':'{}'.format(page)})
      bs = BeautifulSoup(response.text,'html5lib')

      courses = bs.select('div.course-area')
      courses = courses[0].select('div.course-filter-list')
      courses = courses[0].findAll('a')

      for a_tag in courses:
         title = a_tag.select('h2')[0].text
         result.append(['=HYPERLINK("{}","{}")'.format(a_tag['href'],title), cat[0], '', ''])
         i += 1

   band_dataFrame = pd.DataFrame(result,
                                 columns=['عنوان', 'دسته یک', 'دسته دو', 'دسته سه'],
                                 index=range(1, len(result) + 1)
                                 )
   # band_dataFrame.to_csv('DJY.csv')
   band_dataFrame.to_excel('./excel/DJY.xlsx', engine='xlsxwriter')