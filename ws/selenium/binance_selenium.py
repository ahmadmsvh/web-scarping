from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import schedule
import time

driver = webdriver.Chrome()

url = 'https://www.binance.com/en'
driver.get(url)
driver.implicitly_wait(5)

driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

def getLatestNews():
   try:
      driver.get(url)
      driver.implicitly_wait(5)

      driver.find_element( By.LINK_TEXT, 'Announcements' ).click()

      main = driver.find_element( By.CLASS_NAME, 'css-9o1knt' )
      latest_binance_news = main.find_elements(By.CLASS_NAME, 'css-ngahxj')

      latest_binance_news[1].click()

      top_news = driver.find_element(By.CLASS_NAME, 'css-1q4wrpt').find_elements(By.CLASS_NAME,'css-k5e9j4')[0]
      title = top_news.find_element(By.CLASS_NAME,'css-f94ykk').text

      global latest
      latest = 0

      with open('./binance_news.bin', 'r+b') as fp:

         latest = pickle.load(fp)
         print(latest)
         while latest:
            latest = pickle.load(fp)
            print(latest)

         if title != latest:
            with open('./binance_news.bin', 'a+b') as fp:
               pickle.dump(title, fp)
   except:
      pass

schedule.every(5).seconds.do(getLatestNews)

while True:
   schedule.run_pending()
   time.sleep(5)