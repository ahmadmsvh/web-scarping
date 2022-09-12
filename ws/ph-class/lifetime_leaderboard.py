import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.umggaming.com/leaderboards'
response = requests.get(url, 'lxml')
res = response.text

#------------Beautiful soup-----------------
# res1 = response.content
# for byte in res1:
#    print(chr(byte))

# table = BeautifulSoup(res).select('#leaderboard-table')
#
# trs = table[0].select('tr')[1:]
# for tr in trs:
#    print(tr.select('td')[0].text.strip(),' ',tr.select('td')[1].text.strip())


#------------regular expression-----------------
res = re.sub('\n\s*',' ', res)
regex = re.compile('<table id="leaderboard-table"[.\w\W]*</table>')
table = regex.findall(res)

regex = re.compile(r'<tr.*?>(.+?)<\/tr>')
trs = regex.findall(table[0])

tds = []
place = []
user_name = []
regex = re.compile(r'<td.*?>(.+?)<\/td>')
for tr in trs[1:26]:
   tds.append(regex.findall(tr))
   place.append(tds[trs.index(tr)-1][0])
   reg = re.compile(r'<a.*?>(.+?)<\/a>')
   user_name.append(reg.findall(tds[trs.index(tr)-1][1])[1])

for indx in range(len(place)):
   print(place[indx],user_name[indx])





