import requests

def get_1():
    url = "https://xkcd.com/353"

    response = requests.get(url)
    print(response)

#----------

def get_2():
    url = "https://xkcd.com/353"

    response = requests.get(url)
    print(dir(response))

#----------

def get_2_1():
    list = ["C#","JAVA","Swift","C++","C"]
    dic = {}
    print(dir(list))
    print(dir(dic))

#----------

def get_2_2():
    class Order:
        def __dir__(self):
            return ["CustomerName","Product","quantity","Price","Date"]


    myShoppingCard = Order()

    print(dir(myShoppingCard))


# ----------

def get_2_3():
    class Person:
        name = "AmirParsa"
        age = 22
        country = "Iran"

    print(dir(Person))


# ----------

def get_2_4():
    class MyClass:
        x = 0
        y = ""
        def __init__(self,anyNumber,anyString):
            self.x = anyNumber
            self.y = anyString

        def __str__(self):
            return "MyClass( x = " + str(self.x) + ", y = " + self.y +" )"

    obj = MyClass(22,"AmirParsa")

    print(obj.__str__())
    print(obj)
    print(str(obj))

# ----------

def get_3():
    url = "https://xkcd.com/353"

    r = requests.get(url)
    print(help(r))

# ----------

def get_4():
    # url = "https://xkcd.com/353"
    url = "https://golrang.com/"

    response = requests.get(url)
    print(response.text)

# ----------

def get_5():
    url = "https://xkcd.com/comics/python.png"

    response = requests.get(url)
    print(response.content)


# ----------

def get_6():
    url = "https://xkcd.com/comics/python.png"

    response = requests.get(url)
    with open('./Images/'+'PythonComic.png','wb') as fp:
        fp.write(response.content)


# ----------

def get_7():
    url = "https://www.python.org"

    response = requests.get(url)
    print(response.request.headers)

# ----------

def get_8():
    url = "https://www.python.org"

    response = requests.get(url)
    print(response.headers)
    print(response.text)

# ----------

def get_9():
    url = "https://www.crawler-test.com"

    response = requests.get(url)
    print(response.status_code)

# ----------

def get_10():
    url = "https://www.webfx.com/web-development/glossary/http-status-codes/"

    response = requests.get(url)
    print(response.status_code)

# ----------

def get_11():
    url = "https://www.python.org"

    response = requests.get(url)
    print(response.reason)

# ----------

def get_12():
    dict = {"page":2,"count":20}
    url = "http://httpbin.org/get"

    response = requests.get(url,params=dict)
    print(response.url)
    print("========================================")
    print(response.text)


# ----------

def get_13():
    dict = {"username":"admin","password":"pass1234"}
    url = "http://httpbin.org/post"

    response = requests.post(url,data=dict)
    print(response.url)
    print("========================================")
    print(response.text)

# ----------

def get_14():
    dict = {"username":"admin","password":"pass1234"}
    url = "http://httpbin.org/post"

    response = requests.post(url,data=dict)
    print(response.url)

    jsonFile = response.json()
    print("====================json====================")
    print(jsonFile)
    print("====================form====================")
    print(jsonFile["form"])
    print("===================headers=====================")
    print(jsonFile["headers"])

# ----------

def get_15():

    try:
        url = "http://httpbin.org/delay/5"

        response = requests.get(url, timeout=3)
        print(response.text)
        print(response)
    except requests.exceptions.Timeout as e:
        print('time out has been raised')
        print("=================================")
        print(e)

# ----------

def get_16():

    try:
        url = "https://api.Github.com"
        # timeout= (conection,response)
        response = requests.get(url, timeout= (5,7))
        print(response.text)
        print(response)
    except requests.exceptions.Timeout as e:
        print('time out has been raised')
        print("=================================")
        print(e)

# ----------

import time
def get_17():
    url = "http://httpbin.org/"
    time.sleep(5)
    response = requests.get(url)
    print(response.text)
    print(response)

# ----------

# دریافت href خبرها و ذخیره سازی
# https://www.binance.com/en/support/announcement/c-49?avId=49

#--------------------------<<Main Method>>---------------------------------



