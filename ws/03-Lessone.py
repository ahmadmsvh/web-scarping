import pandas as pd
import numpy as np


def Func01():
    list = ['python','C#','C++','C','swift','java']
    df = pd.DataFrame(list)
    print(df)

def Func02():
    list = \
        {
            'Name':['python','C#','C++','C','swift','java'],
            'Age':[12,3,4,10,4,8]
        }
    df = pd.DataFrame(list)
    print(df)


def Func03():
    list = \
        {
            'Name':['python','C#','C++','C','swift','java'],
            'Age':[12,3,4,10,4,8],
            'City': ['Tehran','Tabriz','Esfahan','Yazd','Shiraz','Karaj'],
            'Phone':['091232134','091232434','09123678','091232324','091235696','0912322342']
        }
    df = pd.DataFrame(list)
    print(df[['Name','Phone']])
    print('=======================')
    print(df['City'])
    print('=======================')
    print(df[['City']])


def Func04():
    # data = pd.read_csv('./CSV/nba.csv',index_col='Name')
    data = pd.read_csv('./CSV/nba.csv')
    ages = data[['Age']]
    print(ages)


def Func05():
    # data = pd.read_csv('./CSV/nba.csv',index_col='Name')
    data = pd.read_csv('./CSV/nba.csv')
    ages = data['Age']
    print(ages)


def Func06():
    data = pd.read_csv('./CSV/nba.csv')

    row = data.iloc[1]
    print(row)


def Func07():
    dict = \
        {
            'First Score':[100,40,23,np.nan,80],
            'Second Score': [88, np.nan, 70, 0, np.nan],
            'Third Score': [np.nan, 44, 24, 77 , 96]
        }

    data = pd.DataFrame(dict)
    print(data)
    print('==========================')
    print(data.isnull())


def Func08():
    dict = \
        {
            'First Score':[100,40,23,np.nan,80],
            'Second Score': [88, np.nan, 70, 10, np.nan],
            'Third Score': [np.nan, 44, 24, 77 , 96]
        }

    data = pd.DataFrame(dict)

    data = data.fillna(0)

    print(data)


def Func09():
    dict = \
        {
            'First Score': [100, 40, 23, np.nan, 80],
            'Second Score': [88, np.nan, 70, 10, np.nan],
            'Third Score': [np.nan, 44, 24, 77, 96]
        }

    data = pd.DataFrame(dict)
    print(data)
    print('========================')
    data = data.dropna()
    print(data)


def Func10():
    dict = \
        {
            'Name': ['python', 'C#', 'C++', 'C', 'swift', 'java'],
            'Age': [12, 3, 4, 10, 4, 8],
            'City': ['Tehran', 'Tabriz', 'Esfahan', 'Yazd', 'Shiraz', 'Karaj'],
            'Phone': ['091232134', '091232434', '09123678', '091232324', '091235696', '0912322342']
        }

    data = pd.DataFrame(dict)

    for i,j in data.iterrows():
        # print(i,j)
        # print(f'{i} :\n {j}')
        print(f'{i} :\n {j["Name"]}')
        print()


def Func11():
    dict = \
        {
            'Name': ['python', 'C#', 'C++', 'C', 'swift', 'java'],
            'Age': [12, 3, 4, 10, 4, 8],
            'City': ['Tehran', 'Tabriz', 'Esfahan', 'Yazd', 'Shiraz', 'Karaj'],
            'Phone': ['091232134', '091232434', '09123678', '091232324', '091235696', '0912322342']
        }

    data = pd.DataFrame(dict)

    data_list = list(data)

    for item in data_list:
        print(data[item][2])

# ---------------------------------------
