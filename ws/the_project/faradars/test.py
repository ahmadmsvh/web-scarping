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
        catgs = catgs_table.select('tr')[7:8]

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
            thread.join()

        # new_threads = []
        # new_threads_sub = []
        # thread_counter = 1
        # for thread in threads:
        #     new_threads_sub.append(thread)
        #     if thread_counter%5 == 0:
        #         new_threads.append(new_threads_sub)
        #         new_threads_sub = []
        #     thread_counter += 1
        # new_threads.append(new_threads_sub)
        #
        # for thread_group in new_threads:
        #     for thread in thread_group:
        #         thread.start()
        #     for thread in thread_group:
        #         thread.join()

    def __catCourses(self, catg, cat_url):
        bs = self.__makeRequestBsResponse(cat_url)
        courses = bs.select('item')
        for course in courses[0:10]:
            course_url = course.text.split('\n')[2].strip()
            course_title = course.text.split('\n')[1].strip()

            self.site_dict[catg]['courses'][course_title] = {}
            self.site_dict[catg]['courses'][course_title]['url'] = course_url
            self.site_dict[catg]['courses'][course_title]['title'] = course_title

            bs = self.__makeRequestBsResponse(course_url)
            css = {
                'Teacher': '[name="instructors "] h6',
                'Duration': 'div#durationTitle',
                'Price' : 'div.side.border.rounded.bg-white .col-6',
                'Price-dis': 'div.row.d-flex.justify-content-start ',
                'Discount': None,
                'Students': 'div#soldCount',
                'Status': 'div.text-center.p-3.mb-2.bg-gray + div',
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

            self.site_dict[catg]['courses'][course_title]['Duration'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Duration']).text.strip())

            self.site_dict[catg]['courses'][course_title]['Students'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Students']).text.strip().split('\n')[0])

            self.site_dict[catg]['courses'][course_title]['Price'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Price']).text.strip())

            self.site_dict[catg]['courses'][course_title]['Discount'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Discount']))

            self.site_dict[catg]['courses'][course_title]['Img Url'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Img Url'])['poster'])

            self.site_dict[catg]['courses'][course_title]['Demo Url'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Demo Url']))

            self.site_dict[catg]['courses'][course_title]['Last Update'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Last Update']))

            td = None
            mylist = self.__tryExcept(
                query=lambda: bs.select(css['Language']))
            for tr in mylist:
                if tr.select_one('th').text == 'زبان':
                    td = tr.select_one('td').text.strip().replace(' ', '')
            self.site_dict[catg]['courses'][course_title]['Language'] = td


            self.site_dict[catg]['courses'][course_title]['Subtitle'] = self.__tryExcept(
                query=lambda: bs.select(css['Subtitle']))

            td = None
            mylist = self.__tryExcept(
                query=lambda: bs.select(css['Language']))
            for tr in mylist:
                if tr.select_one('th').text == 'حجم دانلود':
                    td = tr.select_one('td').text.strip().replace(' ', '')
            self.site_dict[catg]['courses'][course_title]['Size'] = td

            self.site_dict[catg]['courses'][course_title]['Website Url'] = 'https://www.faradars.com'

            self.site_dict[catg]['courses'][course_title]['Category'] = catg

            self.site_dict[catg]['courses'][course_title]['Video Quantity'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Video Quantity']).text.strip())

            if self.__tryExcept(query=lambda: bs.select_one(css['Status']).text.split(':')[1]):
                self.site_dict[catg]['courses'][course_title]['Status'] = self.__tryExcept(
                    query=lambda: bs.select_one(css['Status']).text.split(':')[1])
            else:
                self.site_dict[catg]['courses'][course_title]['Status'] = 'در دسترس'


            self.site_dict[catg]['courses'][course_title]['Description'] = self.__tryExcept(
                query=lambda: bs.select_one(css['Description']).text.strip())

    def __makeRequestBsResponse(self, url):
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'html5lib')
        return bs

    def __makePagesUrls(self, url):
        pages_urls = []
        return pages_urls

    def __tryExcept(self, query):
            try:
                return query()
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

        df = pd.DataFrame(df_dict, index=range(1, len(df_dict['title']) +1 ))
        return df

if __name__ == '__main__':
    faradars_url = 'https://faradars.org/rss'
    faradars = Website(faradars_url)
    faradars_df = faradars.makeDataframe()

    with pd.ExcelWriter(f'./{file_name}.xlsx') as writer:
        faradars_df.to_excel(writer, sheet_name='Sheet_1', engine='xlsxwriter')