import requests
import re

response = requests.get('http://www.araas.ir/back-ground-photo/')
home_page_url = response.url

source_string = str(response.content)
source_lines = source_string.split('\\n')

image_tags =[]

for line in source_lines:

   match = re.search('<img',line)
   if match:
      image_tags.append(line.strip())

images_url=[]

counter =0
for img in image_tags:
   counter+=1
   if re.search('src="',img) and re.search('"\s',img):

      start = re.search('src="', img).end()
      img_c = img[start:]
      end = re.search('"\s', img_c).start()

      my_url = img_c[:end]
      if re.findall('^/',my_url):
         my_url = my_url[1:]

      if re.findall('^../', my_url):
         my_url = my_url[3:]

      images_url.append(my_url)
      print(my_url)

      response = requests.get(my_url)
      with open('./image2/'+str(counter)+my_url[-4:], 'wb') as fp:
         fp.write(response.content)


