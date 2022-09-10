import requests
from bs4 import BeautifulSoup
import xlsxwriter
import pandas as pd

categories = []
sub_categories = []
products = []

def category_sub_category():
    url = 'https://toplearn.com/'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    # categories_page = bs.select_one('li.LiCLass')
    sub_category = []
    for item_category in bs.select('li.LiCLass > ul > li'):
        sub_category = []
        categories.append(item_category.select_one('a'))

        x = item_category.select_one('ul')
        if x !=None:
            for item_subcategory in x.select('a'):
                sub_category.append(item_subcategory)
        else:
            sub_category.append(None)

        sub_categories.append(sub_category)

    print('Category And Sub Category Completed ...')

def write_excel_category(file_name):

    col1 = []
    col2 = []
    for i in range(len(sub_categories)):
        x = categories[i].text

        for item in sub_categories[i]:
            if item != None:
                col1.append(x)
                col2.append(item.text)
            else:
                col1.append(x)
                col2.append('None')

    dict = \
        {
            'Categories': col1,
            'Sub Categories': col2
        }
    df = pd.DataFrame(dict)
    writer = pd.ExcelWriter('./Files/'+file_name+'.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Programing Language')
    writer.save()

    print('Excel Category Created ...')

def number_pages(page_url):
    url = 'https://toplearn.com'+page_url
    res = requests.get(url)
    bs = BeautifulSoup(res.text, 'html.parser')
    bigcon = 0
    try:
        con = bs.select_one('div.pagination-layer').select('a')
        if con !=None:
            for i in con:
                if i.text != ' ':
                    if int(i.text) > bigcon:
                        bigcon = int(i.text)
    except:
        if bigcon == 0:
            bigcon += 1
        else:
            bigcon += 1


    return bigcon

def get_product(number_page, cat ,sub_cat):
    number_page += 1;
    for i in range(1, number_page):
        url = 'https://toplearn.com/courses?pageId='+str(i)+'&Search=&orderby=createAndUpdatedate&filterby=all&categories='+sub_cat
        res = requests.get(url)
        bs = BeautifulSoup(res.text, 'html.parser')
        box_count = bs.select('div.course-col')
        for j in bs.select('div.course-col'):
            get_information(j.select_one('a').attrs['href'], cat, sub_cat)

def get_information(url_product, cat ,sub_cat):
    url = 'https://toplearn.com' + url_product
    res = requests.get(url)
    bs = BeautifulSoup(res.text, 'html.parser')
    product = []
    name = bs.select_one('header.course-page-header h1').text
    product.append(name)
    product.append(cat)
    product.append(sub_cat)
    price = bs.select_one('span.course-price del')
    if price == None:
        price = bs.select_one('span.price-amount').text
        product.append(price)
    else:
        product.append(price.text)

    product.append('-')
    product.append(bs.select_one('div.course-details-layer > ul > li > span').text)
    x = bs.select('div.course-details-layer')
    y = x[1].select('li.notShowInRecording')
    product.append(y[1].select_one('span').text)
    product.append(y[0].select_one('span').text)
    product.append(bs.select_one('span.blue-lbl').text)
    products.append(product)
    print(name+' completed ...')

def write_excel(file_name):
    workbook = xlsxwriter.Workbook('./Files/'+file_name+'.xlsx')
    worksheet = workbook.add_worksheet("My sheet")

    worksheet.write('A1', 'Product Name')
    worksheet.write('B1', 'Categories')
    worksheet.write('C1', 'Sub Categories')
    worksheet.write('D1', 'Price')
    worksheet.write('E1', 'Number Of Students')
    worksheet.write('F1', 'Course Instructor')
    worksheet.write('G1', 'Product Duration')
    worksheet.write('H1', 'Number Of Videos')
    worksheet.write('I1', 'Course Status')

    row = 1
    col = 0


    for product, category ,sub_category ,price,number_of_students,course_instructor,product_duration,number_of_videos,course_status in (products):
        worksheet.write(row, col, product)
        worksheet.write(row, col + 1, category)
        worksheet.write(row, col + 2, sub_category)
        worksheet.write(row, col + 3, price)
        worksheet.write(row, col + 4, number_of_students)
        worksheet.write(row, col + 5, course_instructor)
        worksheet.write(row, col + 6, product_duration)
        worksheet.write(row, col + 7, number_of_videos)
        worksheet.write(row, col + 8, course_status)
        row += 1

    print('Excel was created ...')

    workbook.close()

def main():
    category_sub_category()

    for i in range(len(categories)):
        if sub_categories[i]!=[None]:
            for sub_cat in sub_categories[i]:
                number_page = number_pages(sub_cat.attrs['href'])
                get_product(number_page, categories[i].text, sub_cat.text)
        else:
            number_page = number_pages(categories[i].attrs['href'])
            get_product(number_page, categories[i].text, sub_cat.text)
    print('------------------------')
    write_excel('Toplearn')

#--------------------------<<Main Method>>---------------------------------

main()



