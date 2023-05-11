import threading
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

directory_name = os.path.dirname(__file__)
file_name = os.path.basename(__file__).split('.')[0]


class Website:
    def __init__(self, url):
        self.__url = url
        self.site_dict = {}
        self.__products_dict = self.__makeCategories()

    @property
    def url(self):
        return self.__url

    @property
    def products(self):
        return self.__products_dict

    def __makeCategories(self):
        bs = self.__makeRequestBsResponse(self.url)
        catgs_table = bs.select('table')[2]
        catgs = catgs_table.select('tr')[4:]

        for catg in catgs:
            catg_name = catg.select('span')[-1].text
            catg_link = catg.select_one('a')['href']
            self.site_dict[catg_name] = {}
            self.site_dict[catg_name]['courses'] = {}
            self.site_dict[catg_name]['href'] = catg_link

        self.__courses()

    def __courses(self):
        threads = []
        for catg, value in self.site_dict.items():
            trd = threading.Thread(target=self.__catCourses, args=[catg, value['href']])
            threads.append(trd)

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        # print(json.dumps(self.site_dict, indent=4))
    def __catCourses(self, catg, cat_url):
        bs = self.__makeRequestBsResponse(cat_url)
        courses = bs.select('item')
        for course in courses:
            course_url = course.text.split('\n')[2].strip()
            course_title = course.text.split('\n')[1].strip()

            self.site_dict[catg]['courses'][course_title] = {}
            self.site_dict[catg]['courses'][course_title]['url'] = course_url
            self.site_dict[catg]['courses'][course_title]['title'] = course_title

            bs = self.__makeRequestBsResponse(course_url)
            css = {
                'Teacher': '[name="instructors "] h6',
                'Duration': 'div#durationTitle',
                'Price': 'div.row.d-flex.justify-content-start ',
                'Discount': None,
                'Students': 'div#soldCount',
                'Status': None,
                'Last Update': None,
                'Description': 'section#course-navigation-summary div div div p',
                'Video Quantity': 'section.mt-5.pt-3.pb-3.pr-3 div strong',
                'Img Url': '[poster^="https"]',
                'Demo Url': 'video *',
                'Language': 'table.shop_attributes tbody tr',
                'Size': 'table.shop_attributes tbody tr',
                'Subtitle': None,
                'Category': catg
            }

            print(self.site_dict[catg]['courses'][course_title]['url'] )

            self.site_dict[catg]['courses'][course_title]['Teacher'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Teacher']).text)
            # print(self.site_dict[catg]['courses'][course_title]['Teacher'])

            self.site_dict[catg]['courses'][course_title]['Duration'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Duration']).text)
            # print(self.site_dict[catg]['courses'][course_title]['Duration'])

            self.site_dict[catg]['courses'][course_title]['Students'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Students']))
            # print(self.site_dict[catg]['courses'][course_title]['Students'])

            self.site_dict[catg]['courses'][course_title]['Price'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Price']).text.strip())
            # print(self.site_dict[catg]['courses'][course_title]['Price'])

            self.site_dict[catg]['courses'][course_title]['Discount'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Discount']))
            # print(self.site_dict[catg]['courses'][course_title]['Discount'])

            self.site_dict[catg]['courses'][course_title]['Img Url'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Img Url'])['poster'])
            # print(self.site_dict[catg]['courses'][course_title]['Img Url'])

            self.site_dict[catg]['courses'][course_title]['Demo Url'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Demo Url']))
            # print(self.site_dict[catg]['courses'][course_title]['Demo Url'])

            self.site_dict[catg]['courses'][course_title]['Last Update'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Last Update']))
            # print(self.site_dict[catg]['courses'][course_title]['Last Update'])

            self.site_dict[catg]['courses'][course_title]['Language'] = self.__tryExcept(
                query=lambda: bs.select(css['Language']), prop='زبان')
            # print(self.site_dict[catg]['courses'][course_title]['Language'])

            self.site_dict[catg]['courses'][course_title]['Subtitle'] = self.__tryExcept(
                query=lambda: bs.select(css['Subtitle']))
            # print(self.site_dict[catg]['courses'][course_title]['Subtitle'])

            self.site_dict[catg]['courses'][course_title]['Size'] = self.__tryExcept(
                query=lambda: bs.select(css['Size']), prop='حجم دانلود')
            # print(self.site_dict[catg]['courses'][course_title]['Size'])

            self.site_dict[catg]['courses'][course_title]['Website Url'] = 'https://www.faradars.com'
            # print(self.site_dict[catg]['courses'][course_title]['Website Url'])

            self.site_dict[catg]['courses'][course_title]['Category'] = catg
            # print(self.site_dict[catg]['courses'][course_title]['Category'])

            self.site_dict[catg]['courses'][course_title]['Video Quantity'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Video Quantity']).text.strip())
            # print(self.site_dict[catg]['courses'][course_title]['Video Quantity'])

            self.site_dict[catg]['courses'][course_title]['Status'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Status']))
                # print(self.site_dict[catg]['courses'][course_title]['Status'])

            self.site_dict[catg]['courses'][course_title]['Description'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Description']).text.strip())
            # print(self.site_dict[catg]['courses'][course_title]['Description'])

    def __makeRequestBsResponse(self, url):
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'html5lib')
        return bs

    def __makePagesUrls(self, url):
        pages_urls = []
        return pages_urls

    def __tryExcept(self, query, prop=''):
        if prop == '':
            try:
                return query()
            except:
                return None
        else:
            try:
                td = None
                mylist = query()
                for tr in mylist:
                    if tr.select_one('th').text == prop:
                        td = tr.select_one('td').text.strip().replace(' ', '')
                return td
            except:
                return None

    def makeDataframe(self):
        df_dict = {}
        for cat,cat_value in self.site_dict.items():
            for course, course_value in cat_value['courses'].items():
                for col, col_value in course_value.items():
                    try:
                        df_dict[col].append(col_value)
                    except:
                        df_dict[col] = [col_value]

        df = pd.DataFrame(df_dict)
        return df

if __name__ == '__main__':
    faradars_url = 'https://faradars.org/rss'
    faradars = Website(faradars_url)
    faradars_df = faradars.makeDataframe()

    with pd.ExcelWriter(f'./{file_name}.xlsx') as writer:
        faradars_df.to_excel(writer, sheet_name='Sheet_1', engine='xlsxwriter')