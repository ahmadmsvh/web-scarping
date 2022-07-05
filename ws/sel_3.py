from selenium.webdriver.common.print_page_options import PrintOptions
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")

print_options = PrintOptions()
print_options.page_ranges = ['1']

driver.get("printPage.html")

base64code = driver.print_page(print_options)
