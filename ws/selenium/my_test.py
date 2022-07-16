from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome()

# driver.get("https://google.com")
# driver.get("https://www.selenium.dev/documentation/webdriver/browser/navigation/")
# driver.get("https://google.com")
# driver.get("https://www.selenium.dev/documentation/webdriver/browser/alerts/")

# driver.find_element(By.LINK_TEXT,'See an example alert').click()
# wait = WebDriverWait(driver, 1)
# alert = wait.until(EC.alert_is_present())
# text = alert.text
# print(text)
# alert.accept()

# driver.back()
# driver.forward()
# driver.refresh()
# print(driver.title)
# print(driver.current_url)

# # Navigate to url
# driver.get("http://www.example.com")
# # Adds the cookie into current browser context
# driver.add_cookie({"name": "foo", "value": "bar"})
# driver.add_cookie({"name": "foo", "value": "value", 'sameSite': 'Strict'})
# driver.add_cookie({"name": "foo1", "value": "value", 'sameSite': 'Lax'})
# # Get cookie details with named cookie 'foo'
# print(driver.get_cookie("foo"))
# print(driver.get_cookies())
# driver.delete_cookie("test1")
# driver.delete_all_cookies()



# driver.implicitly_wait(0.5)
#
# search_box = driver.find_element(by=By.NAME, value="q")
# search_button = driver.find_element(by=By.NAME, value="btnK")
#
# search_box.send_keys("Selenium")
# search_button.click()
#
# driver.back()
# driver.forward()

# driver.quit()

#     # Navigate to url
# driver.get("http://www.google.com")
#
#     # Enter "webdriver" text and perform "ENTER" keyboard action
# driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

# # Navigate to url
# driver.get("http://www.google.com")
# # Store 'SearchInput' element
# SearchInput = driver.find_element(By.NAME, "q")
# SearchInput.send_keys("selenium")
# SearchInput.submit()
## Clears the entered text
# SearchInput.clear()



