import os.path
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options

url = 'https://www.pelak.com'

# options = Options()
# options.headless = False
# driver = webdriver.Chrome(options=options)
# driver.set_window_position(1000, 500)
# response = driver.get(url)
# print(type(response))
# driver.implicitly_wait(20)

# driver.close()
response = requests.get(url)
print(response)
