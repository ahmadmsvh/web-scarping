import requests
from bs4 import BeautifulSoup

url = 'https://www.alibaba.com/Vehicles-Transportation_p201275273?spm=a2700.8293689.allinfo.d201275273.3cb967afFvbo8g&tracelog=ICBU_PC_HOME_BANNER_LEFT'

response = requests.get(url)
bs = BeautifulSoup(response.text,'html.parser')

recomended = bs.select('div[data-spm-max-idx]')
print(recomended)