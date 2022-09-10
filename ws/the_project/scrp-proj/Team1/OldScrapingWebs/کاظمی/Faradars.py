import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import numpy as np


def futureTutorials(items):
    all_items = []
    for rss_item in items:
        try:
            # product title
            title = rss_item.find('title').text.strip()

            # product description
            description = rss_item.find('description').text.strip()

            # product page link
            product_url = rss_item.find('guid').text.strip()

            # Send request to product page
            product_page_text = requests.get(product_url).text
            bs_product_page = BeautifulSoup(product_page_text, 'lxml')

            # product availability
            available_text = ''
            try:
                available_text = bs_product_page.find('meta', {'property': 'faradars:available'})['content']
            except:
                available_text = np.nan
                print(title, 'available_text')

            if 'موجود است.' in available_text:
                available = True
                release_status = 'موجود است'
            else:
                available = False
                release_status = 'موجود نیست'

            data = \
                {
                    "Title": title,
                    "Category": 'فرادرس های در حال برنامه ریزی',
                    "Description": description,
                    "Publisher": 'فرادرس',
                    "Link": product_url,
                    "Release Status": release_status
                }

            all_items.append(data)
        except:
            continue

    return all_items


def scrapingRss():


    # Request to get data
    url = "https://faradars.org/rss/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")


    table_tag = bs.select("div.row.justify-content-between table.table")[1]
    # table_tag = bs.select("table.table")[1]

    tr_tags = []
    tr_tags.extend(table_tag.select("tr"))
    del tr_tags[0:2]

    xlsx_file = open('./Excel/Faradars/Faradars.xlsx', 'wb')
    writer = pd.ExcelWriter(xlsx_file, engine='xlsxwriter')

    all_data = []
    for tr_tag in tr_tags:
        # clear Previous category Data
        all_data.clear()

        # get Category Title
        td_first_tag = tr_tag.select_one("td")
        category = td_first_tag.select_one("span:last-child").text.strip()
        # .replace("مجموعه آموزش", "")

        # get each category page link
        td_last_tag = tr_tag.select_one("td:last-child")
        href = td_last_tag.find('a').attrs['href']

        # Send request to selected category page link
        rss_response = requests.get(href)
        rss_bs = BeautifulSoup(rss_response.text, "html.parser")

        # get all products in selected category
        rss_items = rss_bs.findAll('item')


        # get details from each product in selected category
        if(category == 'فرادرس های در حال برنامه ریزی'):
            all_data.extend(futureTutorials(rss_items))
        else:
            for rss_item in rss_items:
                try:
                    # product title
                    title = rss_item.find('title').text.strip()

                    # product description
                    description = rss_item.find('description').text.strip()

                    # product page link
                    product_url = rss_item.find('guid').text.strip()

                    # Send request to product page
                    product_page_text = requests.get(product_url).text
                    bs_product_page = BeautifulSoup(product_page_text, 'lxml')

                    # product rate
                    rating_count = ''
                    try:
                        rating_count = bs_product_page.find('meta', {'itemprop': 'ratingValue'})['content']
                    except:
                        rating_count = np.nan
                        print(title, 'rating_count')

                    # product availability
                    available_text = ''
                    try:
                        available_text = bs_product_page.find('meta', {'property': 'faradars:available'})['content']
                    except:
                        available_text = np.nan
                        print(title, 'available_text')

                    if 'موجود است.' in available_text:
                        available = True
                        release_status = 'موجود است'
                    else:
                        available = False
                        release_status = 'موجود نیست'

                    # product instructor
                    instructor = ''
                    try:
                        instructor = bs_product_page.find('meta', {'property': 'faradars:instructor'})['content']
                    except:
                        instructor = np.nan
                        print(title, 'instructor')

                    # product release date
                    release_date = ''
                    try:
                        release_date = bs_product_page.find('meta', {'property': 'video:release_date'})['content']
                    except:
                        release_date = np.nan
                        print(title, 'release_date')

                    # product price
                    price = ''
                    try:
                        price = bs_product_page.find('meta', {'property': 'faradars:price'})['content'].replace("تومان",
                                                                                                                "").strip()
                    except:
                        price = np.nan
                        print(title, 'price')

                    if ',' in price:
                        price = price.replace(",", "")
                    # if price == '۰':
                    #     price = 'رایگان'


                    # product sold count (Students)
                    sold_count = ''
                    try:
                        sold_count = bs_product_page.find('div', {'id': 'soldCount'}).text.strip()
                    except:
                        sold_count = np.nan
                        print(title, 'sold_count')

                    if "نفر" in sold_count:
                        sold_count = sold_count.replace("نفر", "").strip()
                    if ',' in sold_count:
                        sold_count = sold_count.replace(",", "")

                    # product duration
                    duration = ''
                    try:
                        duration = bs_product_page.find('div', {'id': 'durationTitle'}).find('span').text.strip()
                    except:
                        duration = np.nan
                        print(title, 'duration')

                    if "ساعت و" in duration:
                        duration = duration.replace("ساعت و", " : ").replace('دقیقه', '').strip()
                    elif "ساعت" in duration:
                        duration = duration.replace("ساعت", " : ").strip() + ' ۰۰'
                    else:
                        duration = '۰۰ : ' + duration.replace('دقیقه', '').strip()

                    # product sessions
                    session = ''
                    try:
                        session = bs_product_page.find('section', {'class': 'mt-5 pt-3 pb-3 pr-3'}).find(
                            'strong').text.strip()
                    except:
                        session = np.nan
                        print(title, 'session')

                    # Set the correct format
                    data = \
                        {
                            "Title": title,
                            "Category": category,
                            "Price": price,
                            "Duration": duration,
                            "Session": session,
                            "Instructor": instructor,
                            "Rating Count": rating_count,
                            "Sold Count": sold_count,
                            "Available": available,
                            "Release Date": release_date,
                            "Description": description,
                            "Publisher": 'فرادرس',
                            "Link": product_url,
                            "Release Status": release_status
                        }
                    # break
                    all_data.append(data)
                    # print(data)
                except:
                    continue


        band_dataFrame = pd.DataFrame(all_data)
        file_name = "Faradars"
        if "|" in category:
            file_name = category.replace("|", " ")
        else:
            file_name = category

        if len(file_name) > 31:
            file_name = file_name[0:30]

        band_dataFrame.to_excel(writer, sheet_name=file_name,index=False)
        print(category)
        # if category == 'مجموعه آموزش بورس و تحلیل تکنیکال' :
        #     break

    writer.save()
    writer.close()
    # for tr_tag in tr_tags:
    #     print(tr_tag)


scrapingRss()