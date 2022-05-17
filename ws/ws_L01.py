import requests

def get_1():
    url = "https://xkcd.com/353"

    response = requests.get(url)
    print(response)

#-------------------<<>>--------------------

def get_2():
    url = "https://xkcd.com/353"

    response = requests.get(url)
    print(dir(response))

#-------------------<<>>--------------------

def get_2_1():
    list = ["C#","JAVA","Swift","C++","C"]
    dic = {}
    print(dir(list))
    print(dir(dic))


def get_2_2():
    class Order:
        def __dir__(self):
            return ["CustomerName","Product","quantity","Price","Date"]


    myShoppingCard = Order()

    print(dir(myShoppingCard))

#-------------------<<>>--------------------

def get_2_3():
    class Person:
        name = "AmirParsa"
        age = 22
        country = "Iran"

    print(dir(Person))

#-------------------<<>>--------------------

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

#-------------------<<>>--------------------

def get_3():
    url = "https://xkcd.com/353"

    r = requests.get(url)
    print(help(r))

#-------------------<<>>--------------------

def get_4():
    url = "https://xkcd.com/353"

    response = requests.get(url)
    print(response.text)

#-------------------<<>>--------------------

def get_5():
    url = "https://xkcd.com/comics/python.png"

    response = requests.get(url)
    print(response.content)


#-------------------<<>>--------------------

def get_6():
    url = "https://xkcd.com/comics/python.png"

    response = requests.get(url)
    with open('./Images/'+'PythonComic.png','wb') as fp:
        fp.write(response.content)


#-------------------<<>>--------------------

def get_7():
    url = "https://i.pinimg.com/564x/fa/23/e9/fa23e9eea8d63d12d42383563f2b3942.jpg"

    response = requests.get(url)
    with open('./Images/pintrestTest.jpg','wb') as fp:
        fp.write(response.content)



#-------------------<<Main Method>>--------------------

response = requests.get('https://programmershouse.ir/')
help(response)