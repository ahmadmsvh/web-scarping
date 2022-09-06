import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

directory_name = os.path.dirname(__file__)
file_name = os.path.basename(__file__).split('.')[0]

class Website:
    def __init__(self,url):
        self.__products_url = url
        self.__pages_url = self.__makePagesUrls(url)
        self.__products_urls = self.__collectProducts(self.__pages_url)
        self.__courses_details = self.__collectCoursesData(self.__products_urls)

    @property
    def courseDetails(self):
        return self.__courses_details

    def __makeRequestBsResponse(self,url):
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'html5lib')
        return bs

    def __makePagesUrls(self,url):
        pages_urls = []
        beautifulsoup = self.__makeRequestBsResponse(url)
        last_page = beautifulsoup.select('a.page-numbers')[-2].text

        for page in range(1,int(last_page)+1):
            pages_urls.append(url + f'page/{page}/')

        return pages_urls

    def __collectProducts(self,pages_urls):
        products_urls =[]
        for url in pages_urls[:3]:
            beautifulsoup = self.__makeRequestBsResponse(url)
            url_products = beautifulsoup.select('div.course-thumbnail-holder>a')
            for a in url_products:
                products_urls.append([a['href']])
                print(a['href'])

        return products_urls

    def __tryExcept(self,query):
        try:
            return query()
        except:
            return None

    def __collectCoursesData(self,products_urls):
        for url in products_urls[:50]:
            beautifulsoup = self.__makeRequestBsResponse(url[0])

            if beautifulsoup.select('div.meta-info-unit').__len__() == 12 : i = 2
            else : i =3

            title = self.__tryExcept(query = lambda : beautifulsoup.select_one('h1.title-page').text)
            teacher = self.__tryExcept(query = lambda : beautifulsoup.select_one('div.name>a>h6').text)
            duration = self.__tryExcept(query = lambda : beautifulsoup.select_one('div.product-meta-info-list').select_one(f'div.meta-info-unit:nth-child({i+1})').text)
            students = None
            price = self.__tryExcept(query = lambda : beautifulsoup.select_one('p.price').select_one('span.amount').text)
            discounted = self.__tryExcept(query = lambda : beautifulsoup.select_one('p.price').select_one('ins').text)
            img_url = self.__tryExcept(query = lambda : beautifulsoup.select_one('video.wp-video-shortcode')['poster'])
            demo_url = self.__tryExcept(query = lambda : beautifulsoup.select_one('div.course-single-gallery').select_one('source')['src'])
            last_update = None
            language = self.__tryExcept(query = lambda : beautifulsoup.select_one('div.product-meta-info-list').select_one(f'div.meta-info-unit:nth-child({i})').text)
            subtitle = None
            size = self.__tryExcept(query = lambda : beautifulsoup.select_one('div.product-meta-info-list').select_one(f'div.meta-info-unit:nth-child({i+3})').text)
            website_url = 'https://danup.ir/'
            category = self.__tryExcept(query = lambda : beautifulsoup.select_one('nav.woocommerce-breadcrumb').select_one(f':nth-child({i+5})').text)
            video_quantity = self.__tryExcept(query = lambda : beautifulsoup.select_one('div.product-meta-info-list').select_one(f'div.meta-info-unit:nth-child({i+2})').text)
            status = 'available'
            description = self.__tryExcept(query = lambda : beautifulsoup.select_one('div.wpb_wrapper>h2~p').text)

            url.extend([title,teacher,duration,students,price,discounted,
                        img_url,demo_url,last_update,language,subtitle,
                        size,website_url,category,video_quantity,status,
                        description])

        return products_urls

    def makeDataframe(self, list):
        df = pd.DataFrame(list, columns=['Course Url', 'Title', 'Teacher', 'Duration', 'Student', 'Price',
                                         'Discount', 'img Url', 'Demo Url', 'Last Update', 'Subtitle',
                                         'Language', 'Size', 'Website Url', 'Category', 'Video Quantity',
                                         'Status', 'Description'],
                                index=range(1, len(list) + 1))
        return df


if __name__ == '__main__':

    danup_url = 'https://danup.ir/course-category/programming/'
    danup = Website(danup_url)
    result = danup.courseDetails
    dataframe = danup.makeDataframe(result)

    with pd.ExcelWriter(f'./{file_name}.xlsx') as writer:
        dataframe.to_excel(writer, sheet_name='Sheet_1', engine='xlsxwriter')