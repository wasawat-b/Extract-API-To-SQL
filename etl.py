import requests
import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv()

from queries import *

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST")

    MYSQL_PORT = int(os.getenv("MYSQL_PORT"))

    MYSQL_USER = os.getenv("MYSQL_USER")

    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

    MYSQL_DB = os.getenv("MYSQL_DB")

    MYSQL_CHARSET = os.getenv("MYSQL_CHARSET")

fin_list_API = "https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=d4df542295c7f15f66eb88f4a642573a"
his_div_API = "https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/AAPL?apikey=d4df542295c7f15f66eb88f4a642573a"
delist_com_API = "https://financialmodelingprep.com/api/v3/delisted-companies?page=0&apikey=d4df542295c7f15f66eb88f4a642573a"

def finance_list_data(connect, cursor, pathAPI):
    req = requests.get(pathAPI)
    result_list = req.json()
    df = pd.DataFrame(result_list)
    df.columns = ['symbol']

    df.to_csv('historical_dividend.csv', index = False)

    for row in df.iterrows():
        cursor.execute(fin_table_insert, tuple(row))
    
    connect.commit()


def historical_dividend_data(connect, cursor, pathAPI):
    req = requests.get(pathAPI)
    result_list = req.json()
    df = pd.DataFrame(result_list)

    df_extra = pd.DataFrame([x for x in df['historical']])
    column_list = ['date', 'label', 'adjDividend', 'dividend', 'recordDate', 'paymentDate', 'declarationDate']

    for x in column_list:
        df[x] = df_extra[x]

    df_transform = df.drop(['historical'], axis = 1)

    for row in df_transform.iterrows():
        cursor.execute(fin_table_insert, tuple(row))
    
    connect.commit()


def delist_company_data(connect, cursor, pathAPI):
    req = requests.get(pathAPI)
    result_list = req.json()
    df = pd.DataFrame(result_list)

    for row in df.iterrows():
        cursor.execute(fin_table_insert, tuple(row))
    
    connect.commit()

def main():
    connect = pymysql.connect(
                host = Config.MYSQL_HOST,
                port = Config.MYSQL_PORT,
                user = Config.MYSQL_USER,
                password = Config.MYSQL_PASSWORD,
                db = Config.MYSQL_DB,
                charset = Config.MYSQL_CHARSET,
                cursorclass = pymysql.cursors.DictCursor
            )

    cursor = connect.cursor()

    finance_list_data(connect, cursor, fin_list_API)
    historical_dividend_data(connect, cursor, his_div_API)
    delist_company_data(connect, cursor, delist_com_API)

    connect.close()

if __name__ == "__main__":
    main()