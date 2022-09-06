import pandas as pd
import numpy as np
import xlsxwriter


def func01():
    dict = \
        {
            'data':['python', 'C#', 'C++', 'C', 'swift', 'java']
        }

    df = pd.DataFrame(dict)

    writer = pd.ExcelWriter('./excel/01-Test.xlsx')
    # writer = pd.ExcelWriter('./XLSX/01-Test.xlsx',engine='xlsxwriter')

    df.to_excel(writer,sheet_name='Programing Language')

    writer.save()

# ---------------------------------------
def func02():
    dict = \
        {
            'data':['python', 'C#', 'C++', 'C', 'swift', 'java']
        }

    df = pd.DataFrame(dict)

    # writer = pd.ExcelWriter('./XLSX/01-Test.xlsx')
    writer = pd.ExcelWriter('./excel/02-Test.xlsx',engine='xlsxwriter')

    df.to_excel(writer,sheet_name='Programing Language')

    writer.save()


if __name__ == '__main__':
    pass