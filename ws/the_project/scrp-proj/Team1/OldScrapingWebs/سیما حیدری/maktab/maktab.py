import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import os.path

list_main_cat = []
# list_sub_cat_all = []
res_titles_all = []
cat_main = ''

def calculate_page_number(url_sub_cat):
    response = requests.get(url_sub_cat)
    bs = BeautifulSoup(response.text, 'html.parser')

    len_pagination = 1
    div_page = bs.find('div', {"class": "paginator__links"})
    if div_page != None:
        page = div_page.findAll('a')[-1]
        len_pagination = page.text

    return len_pagination

def find_titles(url_sub_cat):
    # find number of pages
    len_page = calculate_page_number(url_sub_cat)

    titles = []
    i = 1
    while i <= int(len_page):
        url = url_sub_cat
        url = url + '?p=' + str(i)

        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'html.parser')

        for item in bs.findAll('div', {"class": "course-card__title"}):
            titles.append(item.text.strip())

        for item in bs.findAll('div', {"class": "course-card__title--career"}):
            titles.append(item.text.strip())
        i += 1

    return titles

def find_subcat(cat_url):
    # -----------------------------sub categories ----------------------------
    list_sub_href = []
    domain = 'https://maktabkhooneh.org'
    list_sub_cat = []

    response = requests.get(cat_url)
    bs = BeautifulSoup(response.text, 'html.parser')

    cat_sub_main = bs.find('h1', {'class': 'category-banner__title'})

    div_tags = bs.findAll('div', {'class': 'white-cell filler--padded bottom-margin'})

    if len(div_tags) != 2 and bs.find('div', {'class': 'carousel__title'}) == None :
        res_titles_result = bs.find_all('div', {'class': 'course-card__title'})

        res_titles = []
        cources_data1 = []

        for item in res_titles_result:
            res_titles.append(item.text)

        cource_result1 = pd.ExcelWriter("NoCategory_" + random.randint(0, 1000).__str__() + '.xlsx')

        cources_data1 = pd.DataFrame({'نام دوره': res_titles,
                                     'دسته بندی وبسایت اصلی': [cat_main.text.replace('موضوعات', '').strip()] * len(res_titles),
                                     'دسته بندی سطح یک': [cat_sub_main.text.strip()] * len(res_titles),
                                     'دسته بندی سطح دو': ["Null"] * len(res_titles),
                                     })

        # write titles data to excel
        cources_data1.to_excel(cource_result1)

        # save the titles result excel
        cource_result1.save()
        print('Titles data is successfully written into Excel File')

    else:
        sub_cats = bs.find_all('div', {'class': 'white-cell filler--padded bottom-margin'})[-1]
        a_tags_sub_cat = sub_cats.find_all_next('a', {'class': 'highlighted-keyword__box--bordered'})

        for a_tag_sub in a_tags_sub_cat:
            cources_data = []
            res_titles = []
            list_sub_cat = []


            res_titles = find_titles(domain + a_tag_sub['href'])
            list_sub_cat.append(a_tag_sub.text.strip())

            # cat_main_list = []

            if os.path.exists(a_tag_sub.text.replace("/", "-").strip() + '.xlsx'):
                # writing to Excel
                cource_result = pd.ExcelWriter(a_tag_sub.text.replace("/", "-").strip() + random.randint(0, 1000).__str__() + '.xlsx')

            else:
                # writing to Excel
                cource_result = pd.ExcelWriter(a_tag_sub.text.replace("/", "-").strip() + '.xlsx')

            cources_data = pd.DataFrame({'نام دوره': res_titles,
                                         'دسته بندی وبسایت اصلی': [cat_main.text.replace('موضوعات', '').strip()] * len(res_titles),
                                         'دسته بندی سطح یک': [cat_sub_main.text.strip()] * len(res_titles),
                                         'دسته بندی سطح دو': list_sub_cat * len(res_titles),
                                         })

            # write titles data to excel
            cources_data.to_excel(cource_result)

            # save the titles result excel
            cource_result.save()
            print('Titles data is successfully written into Excel File')

def find_cat(url):

    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    main_cats = bs.find('div', attrs={'class': 'white-cell filler--padded bottom-margin'})

    a_tags_main_cat = main_cats.find_all_next('a', {'class': 'highlighted-keyword__box--bordered'})

    list_main_href = []
    domain = 'https://maktabkhooneh.org'

    global cat_main
    cat_main = bs.find('div', {'class': 'carousel__title'})

    for a_tag in a_tags_main_cat:
        list_main_cat.append(a_tag.text.strip())
        list_main_href.append(domain + a_tag['href'])

    for cat_url in list_main_href:
        find_subcat(cat_url)

def find_main_cat(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html5lib')

    # div_cat = bs.find('div', {'class': 'footer'})
    # div_columns = div_cat.select('div.footer__column2')
     # print(div_columns)
    main_cats_list = [
        'https://maktabkhooneh.org/learn/%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%88-IT-mk58/',
        'https://maktabkhooneh.org/learn/%D8%B2%D8%A8%D8%A7%D9%86-%D9%87%D8%A7%DB%8C-%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C-mk54/',
        'https://maktabkhooneh.org/learn/%D9%85%D8%AF%DB%8C%D8%B1%DB%8C%D8%AA-%DA%A9%D8%B3%D8%A8-%DA%A9%D8%A7%D8%B1-mk35/',
        'https://maktabkhooneh.org/learn/%D9%85%D8%A7%D9%84%DB%8C-%D8%B3%D8%B1%D9%85%D8%A7%DB%8C%D9%87%DA%AF%D8%B0%D8%A7%D8%B1%DB%8C-mk248/',
        'https://maktabkhooneh.org/learn/%D9%85%D9%87%D9%86%D8%AF%D8%B3%DB%8C-mk89/',
        'https://maktabkhooneh.org/learn/%D8%B9%D9%84%D9%88%D9%85-%D9%BE%D8%A7%DB%8C%D9%87-%D9%88-%D9%BE%D8%B2%D8%B4%DA%A9%DB%8C-mk126/',
        'https://maktabkhooneh.org/learn/%D8%B9%D9%84%D9%88%D9%85-%D8%A7%D9%86%D8%B3%D8%A7%D9%86%DB%8C-mk146/',
        'https://maktabkhooneh.org/learn/%D9%87%D9%86%D8%B1-mk1/',
    ]
    return main_cats_list

def main(url):
    main_cat_url_list = find_main_cat(url)

    # for main_cat_url in main_cat_url_list:
    #     find_cat(main_cat_url)

    find_cat(url)

url = "https://maktabkhooneh.org/learn/%D9%87%D9%86%D8%B1-mk1/"
main(url)