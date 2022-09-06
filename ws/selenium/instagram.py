import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


class Instagram:
    def __init__(self,user,password,page):
        self.options = Options()
        self.options.headless = False
        self.driver = webdriver.Chrome(options=self.options)
        self.user = user
        self.password = password
        self.page = page

    def __login(self):
        driver = self.driver
        url = 'https://www.instagram.com/'
        driver.get(url)
        try:
            self.__cookies()
            time.sleep(3)
        except:
            pass
        input_username = driver.find_element(By.NAME,"username")
        input_username.send_keys(self.user)
        input_password = driver.find_element(By.NAME,"password")
        input_password.send_keys(self.password)
        input_submit = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
        input_submit.click()
        time.sleep(3)

    def __cookies(self):
        driver = self.driver
        cookies_btn = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        cookies_btn.click()

    def download_latest_video(self,page):
        self.__login()
        driver = self.driver
        driver.execute_script("window.stop();")
        driver.get('https://www.instagram.com/' + page)
        time.sleep(5)

        # latest_post_xpath = '//*[@id="mount"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]'
        # latest_post = driver.find_element(By.XPATH, latest_post_xpath)
        # latest_post.click()
        time.sleep(150)

if __name__ == '__main__':

    user = 'amsv.associate'
    password = 'pP@123456789'
    page = 'bino.clip'
    insta_session = Instagram(user,password,page)
    insta_session.download_latest_video(page)
    insta_session.driver.close()
