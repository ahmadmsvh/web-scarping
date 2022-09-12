import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Bot:
    def __init__(self,user,password):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.user = user
        self.password = password


    def __login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        driver.maximize_window()

        driver.implicitly_wait(100)

        input_username = driver.find_element(By.NAME,"username")
        input_username.send_keys(self.user)
        input_password = driver.find_element(By.NAME,"password")
        input_password.send_keys(self.password)
        input_submit = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
        input_submit.click()

        save_login_btn= driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        time.sleep(2)
        notif_btn= driver.find_element(By.CLASS_NAME, '_a9_1').click()


    def __like(self,query,post_number):
        driver = self.driver
        url = 'https://www.instagram.com/'+query
        driver.get(url)
        time.sleep(2)

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.END)

        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a').click()

        time.sleep(2)
        i = 1
        while i <= post_number:

            if driver.find_element(By.XPATH,'//div[contains(@class, "_abm0 _abl")]/span/*[contains(@aria-label,"Like")]'):
                time.sleep(2)
                driver.find_element(By.XPATH, '//*[@aria-label="Like"]/parent::div/parent::button').click()
                driver.find_element(By.XPATH, '//*[@aria-label="Next"]/parent::span/parent::div/parent::button').click()
            elif driver.find_element(By.XPATH,'//div[contains(@class, "_abm0")]/span/*[contains(@aria-label,"Unlike")]'):
                time.sleep(2)
                driver.find_element(By.XPATH,'//*[@aria-label="Next"]/parent::span/parent::div/parent::button').click()

            i += 1

        driver.close()

    def login_like_post(self,page,post_number):
        self.__login()
        time.sleep(2)
        self.__like(page,post_number)




# --------------------------------- main ---------------------------------

username = 'bro.8634'
password = '0440928672PKpk'

page = 'alidaei'
post_number = 12

my_bot = Bot(username, password)
my_bot.login_like_post(page,post_number)


