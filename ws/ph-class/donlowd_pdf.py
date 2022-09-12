import requests

# url = "https://www.db-book.com/slides-dir/PDF-dir/ch2.pdf"
url = 'https://programmershouse.ir/Syllabus/Files/SQL%20Server%202.pdf#divPopupViewPDFDialog'

response = requests.get(url,stream=True)
with open('./pdf/sql2.pdf', 'wb') as fp:
   for chunk in response.iter_content(chunk_size=1024):
      if chunk:
         fp.write(chunk)

