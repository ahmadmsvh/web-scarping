# scraping : https://www.exploit-db.com/

def func00():
    import time
    my_time = int(time.time())
    print(my_time)

def func01():
    import requests
    import time

    time = str(int(time.time()))
    url =f'https://www.exploit-db.com/?draw=1&columns[0][data]=date_published&columns[0][name]=date_published&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=download&columns[1][name]=download&columns[1][searchable]=false&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=application_md5&columns[2][name]=application_md5&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=verified&columns[3][name]=verified&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=description&columns[4][name]=description&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=type_id&columns[5][name]=type_id&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=platform_id&columns[6][name]=platform_id&columns[6][searchable]=true&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=author_id&columns[7][name]=author_id&columns[7][searchable]=false&columns[7][orderable]=false&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=code&columns[8][name]=code.code&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=id&columns[9][searchable]=false&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=9&order[0][dir]=desc&start=0&length=15&search[value]=&search[regex]=false&author=&port=&type=&tag=&platform=&_={time}'

    response = requests.get(url)

    print(response.text)


def func02():
    import requests
    import time


    time = str(int(time.time()))
    url =f'https://www.exploit-db.com/?draw=1&columns[0][data]=date_published&columns[0][name]=date_published&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=download&columns[1][name]=download&columns[1][searchable]=false&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=application_md5&columns[2][name]=application_md5&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=verified&columns[3][name]=verified&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=description&columns[4][name]=description&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=type_id&columns[5][name]=type_id&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=platform_id&columns[6][name]=platform_id&columns[6][searchable]=true&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=author_id&columns[7][name]=author_id&columns[7][searchable]=false&columns[7][orderable]=false&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=code&columns[8][name]=code.code&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=id&columns[9][searchable]=false&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=9&order[0][dir]=desc&start=0&length=15&search[value]=&search[regex]=false&author=&port=&type=&tag=&platform=&_={time}'

    _header = {
        'user_agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01'
    }

    response = requests.get(url,headers= _header)

    print(response.text)


def func03():
    import requests
    import time

    time = str(int(time.time()))
    url = f'https://www.exploit-db.com/?draw=1&columns[0][data]=date_published&columns[0][name]=date_published&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=download&columns[1][name]=download&columns[1][searchable]=false&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=application_md5&columns[2][name]=application_md5&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=verified&columns[3][name]=verified&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=description&columns[4][name]=description&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=type_id&columns[5][name]=type_id&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=platform_id&columns[6][name]=platform_id&columns[6][searchable]=true&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=author_id&columns[7][name]=author_id&columns[7][searchable]=false&columns[7][orderable]=false&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=code&columns[8][name]=code.code&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=id&columns[9][searchable]=false&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=9&order[0][dir]=desc&start=0&length=15&search[value]=&search[regex]=false&author=&port=&type=&tag=&platform=&_={time}'

    _header = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01'
    }

    _cookies = requests.get('https://www.exploit-db.com').cookies

    response = requests.get(url, headers=_header,cookies=_cookies)

    print(response.text)


def func04():
    import requests
    import time

    time = str(int(time.time()))
    url = f'https://www.exploit-db.com/?draw=1&columns[0][data]=date_published&columns[0][name]=date_published&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=download&columns[1][name]=download&columns[1][searchable]=false&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=application_md5&columns[2][name]=application_md5&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=verified&columns[3][name]=verified&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=description&columns[4][name]=description&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=type_id&columns[5][name]=type_id&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=platform_id&columns[6][name]=platform_id&columns[6][searchable]=true&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=author_id&columns[7][name]=author_id&columns[7][searchable]=false&columns[7][orderable]=false&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=code&columns[8][name]=code.code&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=id&columns[9][searchable]=false&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=9&order[0][dir]=desc&start=0&length=15&search[value]=&search[regex]=false&author=&port=&type=&tag=&platform=&_={time}'

    _header = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': 'https://www.exploit-db.com/',
        'x-requested-with': 'XMLHttpRequest'
    }

    _cookies = requests.get('https://www.exploit-db.com').cookies

    response = requests.get(url, headers=_header,cookies=_cookies)

    print(response.text)


def func05():
    import requests
    import time

    time = str(int(time.time()))
    url = f'https://www.exploit-db.com/?draw=1&columns[0][data]=date_published&columns[0][name]=date_published&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=download&columns[1][name]=download&columns[1][searchable]=false&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=application_md5&columns[2][name]=application_md5&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=verified&columns[3][name]=verified&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=description&columns[4][name]=description&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=type_id&columns[5][name]=type_id&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=platform_id&columns[6][name]=platform_id&columns[6][searchable]=true&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=author_id&columns[7][name]=author_id&columns[7][searchable]=false&columns[7][orderable]=false&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=code&columns[8][name]=code.code&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=id&columns[9][searchable]=false&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=9&order[0][dir]=desc&start=0&length=15&search[value]=&search[regex]=false&author=&port=&type=&tag=&platform=&_={time}'

    _header = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': 'https://www.exploit-db.com/',
        'x-requested-with': 'XMLHttpRequest'
    }

    _cookies = requests.get('https://www.exploit-db.com').cookies

    response = requests.get(url, headers=_header,cookies=_cookies).json()

    for data in response['data']:
        _id = data['id']
        _description = data['description'][1]
        _type_id = data['type_id']
        _platform_id = data['platform_id']
        _author_id = data['author_id'][1]
        _download_file = f'https://www.exploit-db.com/download/{_id}'

        print(
            f'id : {_id},  '
            f'Title : {_description},  '
            f'Type : {_type_id},'
            f'Platform : {_platform_id},  '
            f'Author : {_author_id},'
            f'File : {_download_file},  '
            f'\n'
        )


# -----------------------------------main-----------------------------------

func05()
