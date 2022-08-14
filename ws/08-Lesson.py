# implicit wait
# EXplicit wait
import time

path = 'C:\\Users\\ASUS\\PycharmProjects\\WebScraping\\Drivers\\chromedriver.exe'

def func01():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://www.google.com/')

    driver.implicitly_wait(100)
    # حداکثر تا 100 ثانیه

    input_search = driver.find_element(By.NAME, 'q')
    input_search.send_keys('python')

    time.sleep(5)

    btn_search = driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.CqAVzb.lJ9FBc > center > input.gNO89b')
    btn_search.click()

    time.sleep(5)

    driver.close()


def func02():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://www.google.com/')

    input_search = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,'q')))

    input_search.send_keys('python')

    btn_search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.CqAVzb.lJ9FBc > center > input.gNO89b')))

    btn_search.click()

    time.sleep(5)

    driver.close()


def func03():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import Select

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://www.google.com/')

    driver.implicitly_wait(100)

    input_search = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,'q')))

    input_search.send_keys('تست روانشناسی')

    btn_search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.CqAVzb.lJ9FBc > center > input.gNO89b')))

    btn_search.click()

    # https://esanj.ir/

    google_url_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rso"]/div[1]/div/div/div[1]/div/a'))).click()

    search_box =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div[1]/div[2]/ul/li[3]/a'))).click()

    btn_search_box =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div[1]/div[2]/ul/li[3]/ul/li[1]/a'))).click()

    start_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div[2]/div/div[4]/div/div/div[2]/a[1]'))).click()


    drop_birth_find = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'age')))

    drop_birth = Select(drop_birth_find)

    drop_birth.select_by_value('1379')


    drop_gender_find = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'gender')))

    drop_gender = Select(drop_gender_find)

    drop_gender.select_by_value('زن')


    start_test_2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="start-exam-form"]/div[2]/button'))).click()



    for i in range(97):
        if i%2 == 1:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/div[3]/label[1]'))).click()
        else:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/div[3]/label[2]'))).click()

    end_test = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/div[4]/button[4]'))).click()

    show_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/button'))).click()


    time.sleep(5)

    driver.close()


# -------------------------------Main-----------------------------

func03()