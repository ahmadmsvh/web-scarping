import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://faradars.org/explore'

response = requests.get(url)

bs = BeautifulSoup(response.text, 'html5lib')

page_number = bs.select('li.page-item')
last_page = int(page_number[len(page_number)-2].text)

page_urls = [url+'?page={}'.format(i) for i in range(1,range(last_page+1))]

lesson_urls = []

for url in page_urls:
   response = requests.get(url, 'html5lib')
   bs = BeautifulSoup(response.text, 'html5lib')
   lessons = bs.select('div.course-card.grid-item.upcoming_style.treasure.treasure-color')

   for lesson in lessons:
      lesson_urls.append(lesson.find('a')['href'])



   # print(lessons_url)
   #
# result = []
# categories_list = []
#
# for url in urls:
#    response = requests.get(url)
#
#    bs = BeautifulSoup(response.text, 'html5lib')
#    page_numbers_ul = bs.select('ul.page-numbers')
#
#    if len(page_numbers_ul) > 0:
#       tags = page_numbers_ul[0].findAll('li')
#       last_page_tag = tags[len(tags) - 2]
#       number = last_page_tag.find('a').text
#       number_of_pages = int(number)
#    else:
#       number_of_pages = 1
#
#    titles = []
#
#    for page in range(1, number_of_pages + 1):
#       response = requests.get(url, params={'page': '{}'.format(page)})
#       bs = BeautifulSoup(response.text, 'html5lib')
#
#       courses = bs.select('div.course-area')
#       courses = courses[0].select('div.course-filter-list')
#       courses = courses[0].findAll('a')
#
#       cat_1 = bs.select('div.breadcrumbs')[0].findAll('a')[1].text
#       cat_2 = bs.select('div.breadcrumbs')[0].find('strong').text
#
#       for a_tag in courses:
#          title = a_tag.select('h2')[0].text
#          result.append(['=HYPERLINK("{}","{}")'.format(a_tag['href'], title), cat_1, cat_2])
#
#          if [cat_1,cat_2] not in categories_list:
#             categories_list.append([cat_1,cat_2])
#
# titles = pd.DataFrame(result,
#                       columns=['عنوان', 'دسته یک', 'دسته دو'],
#                       index=range(1, len(result) + 1)
#                       )
#
# cats = pd.DataFrame(categories_list,
#                     columns=['دسته یک', 'دسته دو'],
#                     index=range(1, len(categories_list) + 1)
#                     )
#
# with pd.ExcelWriter('./excel/DJY5.xlsx') as writer:
#    titles.to_excel(writer, sheet_name='Sheet_1', engine='xlsxwriter')
#    cats.to_excel(writer, sheet_name='Sheet_2', engine='xlsxwriter')

# titles.to_csv('DJY.csv')
# titles.to_excel('./excel/DJY4.xlsx', engine='xlsxwriter')