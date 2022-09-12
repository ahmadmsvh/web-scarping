from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://faradars.org'

response = requests.get(url)
bs = BeautifulSoup(response.text, 'html5lib' )
cats = bs.find('div',{'class':'categories mt-0 mt-lg-2'})
cats_a = cats.findAll('a')

cats_urls = list(map(lambda x: (url + x['href']), cats_a))

p_url = cats_urls[0]

response = requests.get(p_url, 'html5lib')
bs = BeautifulSoup(response.text, 'html5lib' )

lessons_a = bs.findAll('a', {'class':'aInherit'})
lessons_urls = list(map(lambda x : x['href'], lessons_a))

lessons_info = []
for lesson_url in lessons_urls:
   response = requests.get(lesson_url, 'html5lib')
   bs = BeautifulSoup(response.text, 'html5lib')
   try:
      title = bs.find('span', {'class':'course-page-title'}).text
      title = '=HYPERLINK("{}","{}")'.format(lesson_url, title)
   except Exception:
      title = ''

   try:
      price = bs.find('div', {'class': 'p-3 row'}).find('span').text.strip()
   except Exception:
      price = ''

   try:
      students = bs.find('div', {'id': 'soldCount'}).text.split()[0]
   except Exception:
      students = ''

   try:
      duration = 'در ' + bs.find('div', {'id':'durationTitle'}).find('span').text.strip()
   except Exception:
      duration =''

   try:
      tutor = bs.find('div', {'class':'pr-3 mt-2 text-justify'}).find('h6').text
   except Exception:
      tutor = ''

   try:
      videos = bs.find('div',{'class':'opened mt-4'}).find('strong').text
   except Exception:
      videos = ''

   print(videos)
   lessons_info.append([title, tutor, videos, duration, students, price])

lesson_df = pd.DataFrame(lessons_info,
             columns= ['عنوان','مدرس','تعداد ویدیو','مدت دوره','تعداد دانشجو','فیمت'],
             index=range(1,len(lessons_info)+1)
             )
lesson_df.to_excel('./excel/faradars.xlsx')