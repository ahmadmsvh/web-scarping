import requests
from bs4 import BeautifulSoup

class Website:

    def __init__(self, website_url, categories_urls ):
        self.website_url = websites_url
        self.categories_urls = categories_urls
        self.course_list = self.scrape()
        self.all_courses = set()

    def scrape(self):
        for url_key in self.categories_urls.keys():

            url = self.categories_urls[url_key]
            print(f'{url_key} : {url}')
            response = requests.get(url)

            bs = BeautifulSoup(response.text, 'html.parser')
            number_of_courses = int(bs.select('span.number-tag')[-1].text)
            # div_tag = bs.findAll('span',{'class': 'number-tag'})
            print(number_of_courses)



if __name__ == '__main__':

    websites_url = 'https://faradars.org/'

    categories_urls = {'programming': 'https://faradars.org/how-to-learn/programming',
                       'web-design': 'https://faradars.org/how-to-learn/web-design-and-programming',
                       'computer-science': 'https://faradars.org/how-to-learn/computer-science-and-engineering',
                       }

    web_site_obj = Website(websites_url, categories_urls)






# response = requests.request("GET", url)
#
# print(response.text)
