# Upgrade pip
# python.exe -m pip install --upgrade pip

#  pip3 install selenium

#  pip3 install webdriver-manager
import time

path = 'C:\\Users\\ASUS\\PycharmProjects\\WebScraping\\Drivers\\chromedriver.exe'

def func01():
    from selenium import webdriver

    # driver = webdriver.Chrome(path)
    driver = webdriver.Chrome()

    url = 'https://www.varzesh3.com/'
    driver.get(url)

    print(driver.title)

def func02():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get('https://www.google.com/')

def func03():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://www.google.com/')

    time.sleep(5)

def func04():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://www.google.com/')

    time.sleep(5)

    driver.get('https://programmershouse.ir/')

    time.sleep(5)

def func05():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://www.google.com/')

    time.sleep(2)

    driver.get('https://programmershouse.ir/')

    time.sleep(2)

    driver.back()

    time.sleep(3)

    driver.forward()

    time.sleep(2)

    driver.close()

def func06():
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

    input_search = driver.find_element(By.NAME,'q')
    input_search.send_keys('python')

    time.sleep(5)

    btn_search = driver.find_element(By.CLASS_NAME,'gNO89b')
    btn_search.click()

    time.sleep(5)

    driver.close()

def func07():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys


    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://programmershouse.ir/Users/Login.aspx?Type=sp')

    input_user_name = driver.find_element(By.ID,"Content_Login2_UserName")
    input_user_name.send_keys('your username')


    input_pass = driver.find_element(By.ID,"Content_Login2_Password")
    input_pass.send_keys('your password')

    time.sleep(3)

    btn_submit = driver.find_element(By.ID,"Content_Login2_LoginButton")
    btn_submit.click()

    time.sleep(5)

    driver.close()

def func08():
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

    input_search = driver.find_element(By.NAME,'q')
    input_search.send_keys('python')

    time.sleep(5)

    btn_search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
    btn_search.click()

    time.sleep(5)

    driver.close()

def func09():
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

    input_search = driver.find_element(By.NAME,'q')
    input_search.send_keys('python')

    time.sleep(5)

    btn_search = driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.CqAVzb.lJ9FBc > center > input.gNO89b')
    btn_search.click()

    time.sleep(5)

    driver.close()

def func10():
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

    input_search = driver.find_element(By.NAME,'q')
    input_search.send_keys('python'+Keys.ENTER)


    time.sleep(5)

    driver.close()
# -------------------------------Main-----------------------------

func10()