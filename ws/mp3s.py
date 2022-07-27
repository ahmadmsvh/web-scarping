import re
import requests
from bs4 import BeautifulSoup

url = 'http://purehumbug.com/shows/2006/1-99/'
response = requests.get(url, 'lxml')
res = response.text

regex = re.compile('HREF=".*?(.+?)\.mp3')
# regex = re.compile('(HREF=").*?(\.mp3)')
a_tags = regex.findall(res)


mp3s = []
domain = "http://purehumbug.com"
for a in a_tags:
   if ' ' not in a:
      a = domain + a + '.mp3'
      mp3s.append(a)

for mp3 in mp3s:
   url = mp3
   file_name = re.findall(r"[a-z]*[_][a-z-']*\.mp3", mp3, flags=re.IGNORECASE )[0]
   print(re.findall(r"[a-z]*[_][a-z-']*\.mp3", mp3, flags=re.IGNORECASE ), mp3)
   response = requests.get(url, stream=True)
   with open('./mp3/{}'.format(file_name), 'wb') as fp:
      for chunk in response.iter_content(chunk_size=1024):
         if chunk:
            fp.write(chunk)