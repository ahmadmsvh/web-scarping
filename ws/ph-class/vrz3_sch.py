import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.varzesh3.com'

response = requests.get(url, 'html.parser')

bs = BeautifulSoup(response.text, 'html.parser')

sched = bs.find('div',{'id':'77'}).select('div.widget-schedual > div')

sched_list = []

for row in sched:
   if row['class'][0] == 'date-seprator':
      day = row.find('h4').text
   else:
      match_url = url + row.find('div', attrs={'class':'fixture-result-match-detail'}).find('a')['href']
      match_host = row.find('div', attrs={'class':'fixture-result-match-host'}).find('a').text
      host_goals = row.find('div', attrs={'class':'fixture-result-match-goals'}).select_one('span.host').text
      match_guest = row.find('div', attrs={'class':'fixture-result-match-guest'}).find('a').text
      guest_goals = row.find('div', attrs={'class':'fixture-result-match-goals'}).select_one('span.guest').text

      sched_list.append([day,match_host,host_goals,guest_goals,match_guest,match_url])

df = pd.DataFrame(sched_list,
                  columns=['روز','میزبان','گل میزبان','گل میهمان','میهمان','لیتک بازی'],
                  index=range(1,len(sched_list)+1)
                  )
df.to_excel('./excel/leage_games.xlsx')