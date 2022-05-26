import requests
from bs4 import BeautifulSoup

response = requests.get('https://courses.tosinso.com/fa?page=2')

bs = BeautifulSoup(response.text, 'html5lib').select_one('div.uk-grid')

print(bs)
