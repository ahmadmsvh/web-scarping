import requests
import pickle

page = 1
items = 1
counter = 0
products = []

# while items != [] :
while page <= 5:
   url = "https://api.digikala.com/v1/categories/mobile-phone/search/?brands%5B0%5D=18&page={}".format(page)
   page += 1
   payload={}
   headers = {
     'Cookie': 'TS01e4b47a=01023105915916b0426d48b420d9869b655d5605405699c6ff6ca324fa3e660842ed66e2021b54e53ec00f3549919d24987c368c54cce429a7a72a326db8afbaa31cdf67f08086c1efaea0999ba45598bedaec9ed8; tracker_glob_new=e5MsnXV; tracker_session=f6tVmZQ'
   }

   response = requests.request("GET", url, headers=headers, data=payload)

   response = response.json()

   items = response['data']['products']

   # for item in items:
   #    counter += 1
   #    title = item['title_en']
   #    title = '{}-'.format(str(counter)) + item['title_en']
   #    img_url = item['images']['main']['url']
   #    print(title.replace('/', '-').replace(' ', '-'))
   #    products.append([title, img_url])
   #    image = requests.get(img_url[0])
   #
   #    with open('./digikala/{}.jpg'.format(title.replace('/', '-').replace(' ', '-')), 'wb') as fp:
   #          fp.write(image.content)

   for item in items:
      counter += 1
      title = item['title_en']
      print(title)
      title = '{}-'.format(str(counter)) + item['title_en']
      prod_url = 'https://www.digikala.com'+ item['url']['uri']
      print(prod_url)
      img_url = item['images']['main']['url']

      products.append([title,prod_url, img_url])
      image ='''
      <div>
         <a href="{}">
            <img src="{}">
         </a>
         <div style="position:relative">
            <a style="position:absolute; top:-200px; left:400px" href="{}" >{}</a>
         </div>
      </div>'''.format(prod_url,img_url[0],prod_url,title)

      with open('./digikala/index.html', 'ab') as fp:
            pickle.dump(image, fp)
