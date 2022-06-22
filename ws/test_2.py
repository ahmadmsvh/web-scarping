from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")

title = driver.title

user_box = driver.find_element(by=By.NAME, value="username")
password_button = driver.find_element(by=By.NAME, value="password")
login_button = driver.find_element(By.CSS_SELECTOR, ".sqdOP,.L3NKy,.y3zKF")

user_box.send_keys("ahmadmsvh")
password_button.send_keys("P@ulleroux1972")

login_button.click()
