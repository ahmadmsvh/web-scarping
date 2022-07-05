import requests
from bs4 import BeautifulSoup
import urllib.parse

url = 'https://dyysg.org.uk/docs.php'
response = requests.get(url)

bs = BeautifulSoup(response.text,'lxml')

a_tags = bs.select('a')

hrefs = []
domain = 'https://www.dyysg.org.uk'
url = 'https://www.dyysg.org.uk'
for a_tag in a_tags:
   try:
         href = a_tag['href']
         if '.pdf' in href:
            if domain in href:
               href = href.replace(domain,'')
            href = urllib.parse.unquote(href)

            hrefs.append(url + urllib.parse.quote(href))

   except:
      pass

for href in hrefs:
   try:
      pdf = requests.get(href, stream=True)
      print(urllib.parse.unquote(href).replace(domain+'/docs/', ''))
      with open('./pdf/{}'.format(urllib.parse.unquote(href).replace(domain+'/docs/','')),'wb') as fp:

         for chunk in pdf.iter_content(chunk_size=1024):
            if chunk:
               fp.write(chunk)
   except:
      pass