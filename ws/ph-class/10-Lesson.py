import json

XHR_path_sample = './HTML/XHR'
fetch_path_sample = './HTML/fetch'


def func01():
    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/todos'

    response = requests.get(url)

    page_json = json.loads(response.text)
    print(type(response.text))

    print(type(page_json))
    print('==============================================')
    print(page_json[:2])


def func02():
    import json
    import requests

    deserializing_JSON_sample = './Word/deserializing_serializing_JSON.docx'

    a = {
        "name" : "Amirparsa",
        "age":22,
        "salary" : 500000
    }

    a_json = json.dumps(a)

    print(type(a_json))
    print('==============================================')
    print(a_json)


def func03():
    import json
    import requests
    from bs4 import BeautifulSoup
    deserializing_JSON_sample = './Word/deserializing_serializing_JSON.docx'
    # dynamic page

    url = 'http://quotes.toscrape.com/js/'

    response = requests.get(url)
    page = BeautifulSoup(response.text,"html.parser")

    title = page.find('span',{'class':'text'})

    print(title)

def func04():
    import re

    s = "Black, blue and brown"

    pattern = r"((bl)(\w+))"
    match = re.findall(pattern=pattern,string=s,flags=re.IGNORECASE)

    print(match) # [('Black', 'ack'), ('blue', 'ue')]

    #(.+?);


def func05():
    import json
    import requests
    import re
    from bs4 import BeautifulSoup

    # dynamic page
    url = 'http://quotes.toscrape.com/js/'

    response = requests.get(url)
    js_page = BeautifulSoup(response.text,"html.parser")

    script = js_page.find('script',src=None)

    pattern = "var data =(.+?);\n"
    match = re.findall(pattern=pattern, string=script.string, flags=re.S)
    if match :
        json = json.loads(match[0])

    print(json)

# -------------------------------Main-----------------------------

func05()