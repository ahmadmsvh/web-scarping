from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

url = 'https://www.carsales.com.au'
gt = '1e505deed3832c02c96ca5abe70df9ab'
_2captcha_key = '04123559dee20959d8d618467a406c9d'

driver = webdriver.Chrome()
driver.set_window_position(1000, 500)
driver.get(url)

def solve(driver):
   iframe = driver.find_element(By.TAG_NAME, "iframe")
   driver.switch_to.frame(iframe)
   time.sleep(3)


   old_challenge = driver.find_elements(By.TAG_NAME,'script')[2].get_attribute('src').split('&')[1].split('=')[1]
   print('old challenge: ',old_challenge)

   geetest = driver.find_elements(By.TAG_NAME, 'script')[0].get_attribute('src').split('=')[-1]
   print('geetest: ', geetest)

   spans = driver.find_elements(By.TAG_NAME, "span")
   form_input = driver.find_element(By.TAG_NAME, "form")
   form_inputs = form_input.find_elements(By.TAG_NAME, 'input')

   spans[5].click()
   time.sleep(1)

   new_challenge_url = f"https://api-na.geetest.com/reset.php?gt=1e505deed3832c02c96ca5abe70df9ab&lang=en&challenge={old_challenge}&w=4IR3P5Y17wiFfojAllliJRxmEVrdLm62apgfZv8CbVS4dzzazJHLG4maMoSQGKWDarbHtjfIoR4i5jvN2QEUZTbOtX(GOrpySS96GMXX4sYY9mWujkoP8JKN1Fd6FiuthXxiNT5vuo7YImhdXu8sWZw5GNFAzdZpXoBZeXQi9acfs7UPQWMPDcnDhtMXv5BYYIHYcCmUpdOLkqNXGmQovzt8oi97dBBL38CRaM07a20NYR(9BjqSt9Li5JpDI2HqB4x3UAn)NLMEezAaYDbm9n5SLG(m6ck58zMtNBC0cqfPE7zTmFgKRB7pyj9gH8aUcymMBdO6mchj95G1Dah0)WpP4YO7MSHKepMCk8dVXCac4XsHwfOgjf0LatN7quV4G01Mf9P00cFuHPc29shnhMQaDuO(9doikFNK8bqJmARBhrB(wIkcOhcdkrJc6v4yTnTXV00nA2dn2h6)E2Mv6H)CUK2KnJRvC8aFyrf4tSnfBH7GPWV6AmMfs7TJP2AAPJfHYAeeOgzS2lW1De1)CvGkv1rv5SDG0B6HF6wVrixV6pqwYhA0UzUUDBp8dGXHpFh3GSzezXX0VaAdBPy3veNjpIcYJA)VjhBjdyDKQmQD02Kf2XssFug2sVVCg5yf2uk)eYcEhz)rQoHp)cbevZTiyBKNk1ShG0SQ0rUU71npkjJMT9DTaE)oDfGg0cqUjOpiutntLmak98nWrmWDr0m8dWlZuHD6NgoQa2vV3Mqso2BXosWcTZYWFzOUXv77OEOq8gFxf2ZSTx1akTKaxsMvaEtwACLYoyCjybAAqmkHX4c0TfVsakuKKAYOXpsTZKd2yNN7X(bElw4DoaRAG0uJBb(Glpiql4k2k86LwVCMgO4dnASehb1nOFlzHdsJmKpXgq8JknkhGi7Jh68MsQ..2c5330506f932db0eb40acafc4db5d4e4e82b489710b412d4a1aa5ee36f5f3172026b14c54caa72a2e4ced37c08efc5b083bfb1d1655f3d7e36c2c0422d3eae2f2f80763729f5977ce5f78943d6601ff45105a7413d47f0e75857d0bfe32fb9d4d6f542b90e58cb52acdbab08660f021bf33a693cde9a2866a816eaf18d07478&pt=0&client_type=web&callback={geetest}"
   payload = {}
   headers = {
      'Cookie': 'GeeTestAjaxUser=18a4d99268fdec863d8b29825a67257f; GeeTestUser=84b2e2bd03c7b4a8715dbf8f26ea31da'
   }
   response = requests.request("GET", new_challenge_url, headers=headers, data=payload)
   new_challenge = response.text.split('"')[9]

   print('new challenge: ', new_challenge)


   geetest_url = f'http://2captcha.com/in.php?key={_2captcha_key}&method=geetest&gt={gt}&challenge={new_challenge}&api_server=api-na.geetest.com&pageurl={url}'
   payload={}
   headers = {}
   response = requests.request("GET", geetest_url, headers=headers, data=payload, timeout= 90)
   captcha_id = response.text.split('|')[-1]
   print('captcha ID: ',captcha_id)
   time.sleep(30)


   final_url = f"http://2captcha.com/res.php?key={_2captcha_key}&action=get&id={captcha_id}"
   payload={}
   headers = {}
   response = requests.request("GET", final_url, headers=headers, data=payload)

   print(response.text)
   print()
   resp = response.text
   driver.refresh()
   return resp

   # challenge_form_input = form_inputs[0].send_keys()
   # validate_form_input = form_inputs[1].send_keys()
   # seccode_form_input = form_inputs[2].send_keys()
   # form_input.submit()

resp = solve(driver)

while resp == 'ERROR_CAPTCHA_UNSOLVABLE':
   resp = solve(driver)