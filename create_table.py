import pymysql
from queries import create_table_queries, drop_table_queries

import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST")

    MYSQL_PORT = int(os.getenv("MYSQL_PORT"))

    MYSQL_USER = os.getenv("MYSQL_USER")

    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

    MYSQL_DB = os.getenv("MYSQL_DB")

    MYSQL_CHARSET = os.getenv("MYSQL_CHARSET")


def connect_database():
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

    return connect, cursor

def drop_tables(connect, cursor):
    for query in drop_table_queries:
        cursor.execute(query)
        connect.commit()

def create_tables(connect, cursor):
    for query in create_table_queries:
        cursor.execute(query)
        connect.commit()

def main():
    connect, cursor = connect_database()

    drop_tables(connect, cursor)
    create_tables(connect, cursor)

    connect.close()

if __name__ == "__main__":
    main()