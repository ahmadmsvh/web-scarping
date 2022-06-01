import pandas as pd
import requests

url = "https://www.udemy.com/api-2.0/course-landing-components/394676/me/?javascript%3As.js%3A78=&components=curriculum_context"

payload={}
headers = {
  'Cookie': '__cf_bm=y1cjo0PVk0qySrKCH5eubGhP8vCZB2KxhYTwpKBQ2uo-1654069979-0-AY0OgzsTBHniHOuIz5sXeI/XymuX8Fcoef/MBBn0M33D+4u010pvctwcS+o5cCB9dq6P68U14tldoiLBM/3f2AU=; __udmy_2_v57r=007bd4f2e708431797c8d085d3663a45; evi="3@Y9988u3A98jrkQYMruur-wX2EabXH80Q68noyv2KWth1lJogXJoRBxXWJyozs-wLIqJqFqg-r6apyJoBiD0gCnimGcTYGBhYpaHeHHG1A4egyJQjFVFaFJQxKl8eE5nabTA="; seen=1; ud_cache_brand=GBen_US; ud_cache_campaign_code=ST4MT53122; ud_cache_device=None; ud_cache_language=en; ud_cache_logged_in=0; ud_cache_marketplace_country=GB; ud_cache_modern_browser=0; ud_cache_price_country=GB; ud_cache_release=aeb566ff7d4df6ef5871; ud_cache_user=""; ud_cache_version=1; ud_firstvisit=2022-06-01T07:52:58.276671+00:00:1nwJA3:7Dj3kMirKuteItkrmeEvDPv3Y00; ud_rule_vars="eJx9jssKwjAURH9FslXLbZ5tvqUQYnJTg49gknYj_rsBRQTB7TBnztxJtXnGit6sscSasgZQB88DRQUDZ70alRs8DMIzKZnlQruUThGJ3pD7RELMpb5Y423FqeUToUDpHuQe-g0oLagWQ0dVz7nYAjTDRHatdbYNrWlxR1OzDSE6U9KSHZrV5mgP5_dayrO9RvcFuVYr-NbWePmj5aCkkj_ajLcFy__PYweil-wDP8jjCXxBWXI=:1nwJA3:bR-twliDs2Iurh1sY6KknZ48zq8"'
}

response = requests.request("GET", url, headers=headers, data=payload)

jsn = response.json()['curriculum_context']['data']['sections']

python_lesson=[]
for title in jsn:
   sub = map(lambda i: (title['items'][i]['title'], title['items'][i]['content_summary']), range(len(title['items'])))
   sub_string = ''
   for i in sub:
      sub_string += i[0]+'  '+i[1]+' | '
   python_lesson.append([title['title'],title['content_length_text'],
                        sub_string[:len(sub_string)-3],
                        ])

course_desc = pd.DataFrame(python_lesson,
             columns=['title','duration','subtitles'],
             index=range(1,len(python_lesson)+1)
             )

course_desc.to_excel('./excel/udemy.xlsx', engine='xlsxwriter')
