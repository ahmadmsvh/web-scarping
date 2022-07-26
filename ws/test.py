import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.umggaming.com/leaderboards'
response = requests.get(url, 'lxml')
res = response.text

# table = BeautifulSoup(res).select('#leaderboard-table')
#
# trs = table[0].select('tr')[1:]
# for tr in trs:
#    print(tr.select('td')[0].text.strip(),' ',tr.select('td')[1].text.strip())



res = re.sub('\n',' ',res)
regex = re.compile('<table id="leaderboard-table".*</table>')
table = regex.findall(res)
print(table)

trs = re.split('<tr>',table[0])[2:-1]

print(trs[0].strip())

for tr in trs:
   tds = re.split('<td>', tr)[2:4]
   print(tds)
