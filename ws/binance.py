import requests

url = "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&pageSize=20&pageNo=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
jsn = response.json()

code = jsn['data']['catalogs'][1]['articles'][0]['code']
print(code)