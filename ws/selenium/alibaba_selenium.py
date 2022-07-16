import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pandas as pd

url = 'https://www.alibaba.com/Vehicles-Transportation_p201275273?spm=a2700.8293689.allinfo.d201275273.3cb967afFvbo8g&tracelog=ICBU_PC_HOME_BANNER_LEFT'

driver = webdriver.Chrome()
driver.get(url)
footer = driver.find_element(By.ID, 'ui-footer')

scroll_condition = True
number_of_products = 0
while scroll_condition:
   ActionChains(driver).scroll_to_element(footer).perform()
   recommended = driver.find_elements(By.CLASS_NAME, 'flex5ColFloor')
   if number_of_products == len(recommended):
      scroll_condition = False
   number_of_products = len(recommended)
   time.sleep(4)

recommended = driver.find_elements(By.CLASS_NAME, 'flex5ColFloor')

counter = 0
recommended_products = []
for product in recommended:
   counter += 1
   product_info = product.find_elements(By.TAG_NAME, 'span')
   recommended_products.append([product_info[0].text, product_info[1].text])

df = pd.DataFrame(recommended_products,
                  columns=['description','fee'],
                  index=range(1, len(recommended_products) + 1))

with pd.ExcelWriter('./alibaba_recommended.xlsx') as writer:
   df.to_excel(writer, sheet_name='Sheet_1', engine='xlsxwriter')