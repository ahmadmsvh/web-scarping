import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options

categories_url = {'programming': 'https://nabegheha.com/shop'}

courses_info = dict()

# def (query):
#     try:
#         return query()
#     except:
#         return None

for category in categories_url.keys():

    courses_info[category] = dict()
    url = categories_url[category]

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(1000, 500)
    driver.get(url)
    driver.implicitly_wait(20)

    container_div = driver.find_element(By.CSS_SELECTOR,'section.cat-shop>.cat-shop__content-top')
    courses = container_div.find_elements(By.CLASS_NAME, 'cat-shop__title')

    for course in courses:
        title = course.find_element(By.TAG_NAME, 'h2').text
        courses_info[category][title] = dict()
        website_url = course.find_element(By.TAG_NAME, 'a').get_attribute('href')

for category in courses_info.keys():
    for title in courses_info[category].keys():

        url = website_url
        print(title,url)
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.set_window_position(1000, 500)
        driver.get(url)
        driver.implicitly_wait(20)

        css = {
            'Teacher' : 'div.education__body>ul>li:nth-child(1)>span',
            'Duration' : 'div.education__body>ul>li:nth-child(2)>span',
            'Price' : '.education__mony',
            'Discount' : None,
            'Students': None,
            'Status' : None,
            'Last Update' : 'div.education__body>ul>li:nth-child(9)>span',
            'Description' : 'div.content-single__training-package span',
            'Video Quantity' : 'div.education__body>ul>li:nth-child(7)>span',
            'Img Url' : 'div.education__sidebar img',
            'Demo Url' : 'div.content-single__video source',
            'Language' : None,
            'Size' : 'div.education__body>ul>li:nth-child(3)>span',
            'Subtitle': None,
            'Category' : category
        }
        # 'Course Url', 'Title', 'Teacher', 'Duration', 'Student', 'Price',
        # 'Discount', 'img Url', 'Demo Url', 'Last Update', 'Subtitle',
        # 'Language', 'Size', 'Website Url', 'Category', 'Video Quantity',
        # 'Status', 'Description'

        courses_info[category][title]['Course Url'] = url
        courses_info[category][title]['Title'] = title
        courses_info[category][title]['Teacher'] = (driver.find_element(By.CSS_SELECTOR, css['Teacher']).text)
        courses_info[category][title]['Duration'] = (driver.find_element(By.CSS_SELECTOR, css['Duration']).text)
        courses_info[category][title]['Student'] = None
        courses_info[category][title]['Price'] = (driver.find_element(By.CSS_SELECTOR, css['Price'] ).text.replace('\n',' '))
        courses_info[category][title]['Discount'] = None
        courses_info[category][title]['Img Url'] = (driver.find_element(By.CSS_SELECTOR, css['Img Url']).get_attribute('src'))
        courses_info[category][title]['Demo Url'] = (driver.find_element(By.CSS_SELECTOR, css['Demo Url']).get_attribute('src'))
        courses_info[category][title]['Last update'] = (driver.find_element(By.CSS_SELECTOR, css['Last Update']).text.replace('\n',' '))
        courses_info[category][title]['Subtitle'] = None
        courses_info[category][title]['Language'] = None
        courses_info[category][title]['Size'] = (driver.find_element(By.CSS_SELECTOR, css['Size']).text)
        courses_info[category][title]['Website Url'] = website_url
        courses_info[category][title]['Category'] = category
        courses_info[category][title]['Video Quantity'] = (driver.find_element(By.CSS_SELECTOR, css['Video Quantity']).text)
        courses_info[category][title]['Status'] = None
        courses_info[category][title]['Description'] = (driver.find_element(By.CSS_SELECTOR, css['Description']).text)



        driver.close()

df = pd.DataFrame(courses_info['programming'].values())
# df = df.transpose()

path = os.path.dirname(__file__)
with pd.ExcelWriter(f'{path}/nabegheha.xlsx') as writer:
   df.to_excel(writer, sheet_name='Sheet_1', engine='xlsxwriter')
   # df.to_excel(writer, sheet_name='Sheet_2', engine='xlsxwriter')
