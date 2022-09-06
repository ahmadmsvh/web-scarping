import time

# SampleForScrollTo = './HTML/WindowScroll.html'

def func01():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options


    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://www.worldometers.info/geography/flags-of-the-world/')

    driver.execute_script('window.scrollTo(0,2000);')

    time.sleep(10)

    driver.close()

def func02():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By


    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://www.worldometers.info/geography/flags-of-the-world/')

    Portugal_flag = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div/div/div[140]')

    driver.execute_script("arguments[0].scrollIntoView()",Portugal_flag)

    time.sleep(10)

    driver.close()

def func03():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By


    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://www.worldometers.info/geography/flags-of-the-world/')

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

    time.sleep(10)

    driver.close()

def func04():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By


    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://quotes.toscrape.com/scroll')

    driver.execute_script('window.scrollTo(0,200);')

    time.sleep(10)

    driver.close()

def func05():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By



    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get('https://quotes.toscrape.com/scroll')

    final_height = driver.execute_script('return document.body.scrollHeight')
    height = driver.execute_script('return document.body.scrollHeight')+1
    while final_height < height :
        final_height = height
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        height = driver.execute_script('return document.body.scrollHeight')

    quotes = driver.find_elements(By.CLASS_NAME,'text')

    for quote in quotes:
        print('===============================================')
        print(quote.text)

    print(len(quotes))

    time.sleep(10)

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

    driver.get('https://quotes.toscrape.com/scroll')

    body = driver.find_element(By.TAG_NAME,"body")

    for i in range(10):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)


    quotes = driver.find_elements(By.CLASS_NAME,'text')

    for quote in quotes:
        print('===============================================')
        print(quote.text)

    print(len(quotes))

    time.sleep(10)

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

    driver.get('https://quotes.toscrape.com/scroll')

    body = driver.find_element(By.TAG_NAME,"body")

    final_height = driver.execute_script('return document.body.scrollHeight')
    height = driver.execute_script('return document.body.scrollHeight')+1
    while final_height < height :
        final_height = height
        body.send_keys(Keys.END)
        time.sleep(3)
        height = driver.execute_script('return document.body.scrollHeight')

    quotes = driver.find_elements(By.CLASS_NAME,'text')

    for quote in quotes:
        print('===============================================')
        print(quote.text)

    print(len(quotes))

    time.sleep(10)

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

    driver.get('https://quotes.toscrape.com/scroll')

    body = driver.find_element(By.TAG_NAME,"body")

    final_height = driver.execute_script('return document.body.scrollHeight')
    height = driver.execute_script('return document.body.scrollHeight')+1
    while final_height < height :
        final_height = height
        body.send_keys(Keys.END)
        time.sleep(3)
        height = driver.execute_script('return document.body.scrollHeight')

    quotes = driver.find_elements(By.CLASS_NAME,'text')

    for quote in quotes:
        print('===============================================')
        print(quote.text)

    print(len(quotes))

    time.sleep(10)

    driver.close()


if __name__ == '__main__':

    func07()