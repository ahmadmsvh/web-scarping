import requests
from bs4 import BeautifulSoup
import html5lib.treeadapters.sax
import lxml
import schedule
from datetime import date
import time


def get_1():
    url = "https://www.crawler-test.com"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,"html.parser")
    print(bs)

#----------

def get_2():
    url = "https://www.crawler-test.com"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,"html.parser")
    first_a_tag = bs.find('a')
    print(first_a_tag)

#----------


def get_3():
    url = "https://www.crawler-test.com"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,"html.parser")
    all_a_tag = bs.findAll('a')
    # all_a_tag = bs.find_all('a')
    print(all_a_tag)

#----------


def get_4():
    url = "https://www.google.com/"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,"html.parser")
    links = bs.findAll('a')

    for link in links:
        if 'Gmail' in link.text:
            print(link)
            print(link.attrs['href'])


#----------


def get_5():
    url = "https://www.whitehouse.gov/briefing-room/"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,"html.parser")

    urls = []
    for h2_tag in bs.findAll('h2'):
        a_tag = h2_tag.find('a')
        if a_tag != None:
            urls.append(a_tag.attrs['href'])

    for url in urls:
        print(url)

#----------


def get_6():
    url = "https://www.whitehouse.gov/briefing-room/"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,"html.parser")

    titles = []
    for h2_tag in bs.findAll('h2'):
        a_tag = h2_tag.find('a')
        if a_tag != None:
            titles.append(a_tag.text.strip())

    for title in titles:
        print(title)

#----------


def get_7():

    html_doc = '''
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                </head>
                <body>
                <a href="https://www.example.com/" class="class1" id="id1">test1</a>
                <a href="https://www.example.com/" class="class1" id="id2">test2</a>
                <a href="https://www.google.com/" class="class1" id="id3">Google Search</a>
                <p class="pclass1" id="pid1">lorem1</p>
                <p class="pclass2" id="pid2">lorem2</p>
                <b class="bclass1" id="bid1">bold1</b>
                <blockquote class="blockclass1" id="blockid1">Extremely bold</blockquote>
                <b class="bclass2" id="bid2">bold2</b>
                <b class="bclass1" id="bid3">bold3</b>
                <p id="pid3">....</p>
                </body>
                </html> 
                '''

    with open('./Files/01-index.html','w') as f:
        f.write(html_doc)

    bs = BeautifulSoup(html_doc, "html.parser")
    # ===================================
    # print(bs)
    # ===================================
    # print(bs.text)
    # ===================================
    # print(bs.prettify())
    # ===================================
    # print(bs.b)
    # ===================================
    # print(bs.find('b'))
    # ===================================
    # print(bs.b.name)
    # ===================================
    tag = bs.b
    # print(tag)
    # tag.name = 'blockquote'
    # print(tag)
    # ===================================
    tag = bs.findAll('b')[1]
    # print(tag)
    # print(tag['id'])
    # print(tag.attrs)
    # ===================================
    tag['id'] = 'newBid2'
    # print(tag)
    # ===================================
    del tag['id']
    del tag['class']
    # print(tag)
    # ===================================
    tag.string.replace_with('new text')
    # print(tag)
    # ===================================


#----------

def get_8():
    url = "https://www.whitehouse.gov/briefing-room/"

    response = requests.get(url)
    bs = BeautifulSoup('<li> <p>',"html.parser")

    print("html.parser")
    print(bs)

#----------

def get_9():
    url = "https://www.whitehouse.gov/briefing-room/"

    response = requests.get(url)
    # Slowest
    bs = BeautifulSoup('<li> <p>','html5lib')

    print("html5lib")
    print(bs)

#----------

def get_10():
    url = "https://www.whitehouse.gov/briefing-room/"

    response = requests.get(url)
    # Fastest
    bs = BeautifulSoup('<li> <p>','lxml')

    print("lxml")
    print(bs)

#----------

def get_11():
    url = "https://www.crawler-test.com"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html5lib')

    find = bs.find('div',attrs={'class':'panel-header'})

    print(find.prettify())

#----------

def get_12():
    url = "https://www.crawler-test.com"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html5lib')

    findAll = bs.findAll('div',attrs={'class':'panel-header'})  #return list

    print(findAll)

#----------

def get_13():
    url = "https://www.crawler-test.com"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html5lib')

    select = bs.select('div.panel-header')    # return list


    print(select)

#----------

def get_14():
    url = "https://www.crawler-test.com"

    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html5lib')

    select_one = bs.select_one('div')

    print(select_one.prettify())

# ----------

def get_15():
    url = "https://www.varzesh3.com/"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html5lib')

    div_tag = bs.find('div',attrs={'class':'widget-header'})
    h2_tag = div_tag.find('h2')

    print(h2_tag.text)

#----------

def get_16():
    url = "https://www.varzesh3.com/"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html5lib')

    div_tag = bs.select_one('div.widget-header')
    h2_tag = div_tag.select_one('h2')

    print(h2_tag.text)

#----------

def get_17():
    url = "https://www.varzesh3.com/"

    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html5lib')

    div_tag = bs.select_one('div.widget-header')
    h2_tag = div_tag.select_one('h2')

    print(h2_tag.text)

#----------

def get_18():
    data =\
        ''' 
            <ul>
                <li class = "item"> item1 </li>
                <li class = "item"> item2 </li>
                <li class = "item"> item3 </li>
            </ul>
        '''

    bs = BeautifulSoup(data,'html5lib')

    li_tags_text = bs.select('li.item')

    for li_text in li_tags_text :
        print(li_text.getText())


#----------

def get_19():
    url ='https://www.varzesh3.com/'

    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html.parser')

    div_tag = bs.find('div',attrs= {'id':'78'})

    print(div_tag)

#----------

def get_20():
    url ='https://www.varzesh3.com/'

    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html.parser')

    div_tag = bs.find('div',attrs= {'id':'78'})

    print(div_tag)

#----------

another_index = 0
def get_21():

    # =============================Counter and Log===============================
    def counter():
        date_log = date.today()
        time_log = time.strftime("%H:%M:%S")
        index = 0
        with open('./files/log_index.txt', 'r') as f:
            last_data = f.readlines()
            if len(last_data) != 0:
                if '-' in last_data[-1]:
                    index = last_data[-1].split('-')[0]
                else:
                    index = last_data[-1]

        print(f'{index}- second')
        index = int(index) + 1

        log_msg = '\n'+str(index)+' - '+ str(date_log) +","+str(time_log)
        with open('./files/log_index.txt', 'a') as f:
            f.write(log_msg)

    # =============================Counter with global variable===============================
    def another_counter():
        global another_index
        print(f'{another_index}- another second')
        another_index = another_index + 1

    def say_hello():
        print('1- hello programmers house student')

    def goodluck():
        print('2- goodluck programmers house student')

    def do_work():
        print('3- do work programmers house student')

    def goodNight():
        print('4- good Night programmers house student')

    def go_work():
        print('5- go work programmers house student')

    def say_msg(msg):
        print(f'6- {msg} programmers house student')

    #=============get_21 Main=============================

    schedule.every().second.do(counter)

    schedule.every().second.do(another_counter)

    schedule.every(5).seconds.do(say_msg,msg = 'Ali')

    schedule.every(1).minutes.do(say_hello)

    schedule.every().hour.do(goodluck)

    schedule.every().day.at('00:00').do(goodNight)

    schedule.every(5).to(10).minutes.do(do_work)

    schedule.every().monday.do(go_work)

    schedule.every().tuesday.at('18:00').do(say_hello)

    # ****
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':

    get_21()


