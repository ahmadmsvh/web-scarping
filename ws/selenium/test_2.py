from selenium import webdriver

with webdriver.Chrome() as driver:

   driver.get("https://www.google.com")
   driver.set_window_position(300,0)
   driver.maximize_window()
   driver.save_screenshot('./image.png')


