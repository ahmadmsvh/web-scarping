import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

categories_url = {'programming': 'https://nabegheha.com/shop'}

courses_info = dict()

for category in categories_url.keys():

    courses_info[category] = dict()
    url = categories_url[category]

    driver = webdriver.Chrome()
    driver.set_window_position(1000, 500)
    driver.get(url)
    driver.implicitly_wait(20)

    container_div = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[1]/div[2]/div')
    courses = container_div.find_elements(By.CLASS_NAME, 'cat-shop__title')

    for course in courses:
        title = course.find_element(By.TAG_NAME, 'h2').text
        courses_info[category][title] = dict()
        courses_info[category][title]['url'] = course.find_element(By.TAG_NAME, 'a').get_attribute('href')

    driver.close()

for category in courses_info.keys():
    for title in courses_info[category].keys():

        url = courses_info[category][title]['url']
        driver = webdriver.Chrome()
        driver.set_window_position(1000, 500)
        driver.get(url)
        driver.implicitly_wait(20)

        xpaths = {
            'teacher' : '/html/body/div/div[1]/div[2]/div[1]/section/div/div[1]/ul/li[1]/span',
            'duration' : '/html/body/div/div[1]/div[2]/div[1]/section/div/div[1]/ul/li[2]/span',
            'price' : '/html/body/div/div[1]/div[2]/div[1]/section/div/div[1]/ul/li[12]/div',
            'discount' : None,
            'students': None,
            'status' : None,
            'last update' : '/html/body/div/div[1]/div[2]/div[1]/section/div/div[1]/ul/li[9]/span',
            'description' : '/html/body/div/div[1]/div[2]/div[2]/section[1]/div[3]/div/p[1]/span',
            'number of videos' : '/html/body/div/div[1]/div[2]/div[1]/section/div/div[1]/ul/li[7]/span',
            'image url' : '/html/body/div/div[1]/div[2]/div[1]/section/div/figure/img',
            'demo url' : '/html/body/div/div[1]/div[2]/div[2]/section[1]/div[1]/video/source',
            'language' : None,
            'size' : '/html/body/div/div[1]/div[2]/div[1]/section/div/div[1]/ul/li[3]/span',
            'subtitle': None,
            'category' : category
        }
        courses_info[category][title]['title'] = title
        courses_info[category][title]['course url'] = url
        courses_info[category][title]['teacher'] = driver.find_element(By.XPATH, xpaths['teacher']).text
        courses_info[category][title]['duration'] = driver.find_element(By.XPATH, xpaths['duration']).text
        courses_info[category][title]['price'] = driver.find_element(By.XPATH, xpaths['price']).text.replace('\n',' ')
        courses_info[category][title]['discount'] = None
        courses_info[category][title]['students'] = None
        courses_info[category][title]['status'] = None
        courses_info[category][title]['last update'] = driver.find_element(By.XPATH, xpaths['last update']).text.replace('\n',' ')
        courses_info[category][title]['description'] = driver.find_element(By.XPATH, xpaths['description']).text
        courses_info[category][title]['number of videos'] = driver.find_element(By.XPATH, xpaths['number of videos']).text
        courses_info[category][title]['image url'] = driver.find_element(By.XPATH, xpaths['image url']).get_attribute('src')
        courses_info[category][title]['demo url'] = driver.find_element(By.XPATH, xpaths['demo url']).get_attribute('src')
        courses_info[category][title]['language'] = None
        courses_info[category][title]['size'] = driver.find_element(By.XPATH, xpaths['number of videos']).text
        courses_info[category][title]['subtitle'] = None
        courses_info[category][title]['category'] = category
        driver.close()

df = pd.DataFrame(courses_info['programming'].values())
# df = df.transpose()

print(df)

path = os.path.dirname(__file__)
with pd.ExcelWriter(f'{path}/nabegheha2.xlsx') as writer:
   df.to_excel(writer, sheet_name='Sheet_1', engine='xlsxwriter')
   # df.to_excel(writer, sheet_name='Sheet_2', engine='xlsxwriter')