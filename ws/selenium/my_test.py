from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://google.com")

title = driver.title

driver.implicitly_wait(0.5)

search_box = driver.find_element(by=By.NAME, value="q")
search_button = driver.find_element(by=By.NAME, value="btnK")

search_box.send_keys("Selenium")
search_button.click()

driver.back()
driver.forward()

# driver.quit()