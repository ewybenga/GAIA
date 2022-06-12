"""
Support functions for communicating with sql from 
 - https://www.sqlitetutorial.net/sqlite-python/creating-tables/
 - https://www.sqlitetutorial.net/sqlite-python/insert/
"""
import sqlite3
from sqlite3 import Error

def clean_data(raw_data):
    return (int(raw_data[0]),)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, table_name, clean=False):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    if clean:
        drop_table(conn, table_name)

    create_table_sql = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                            id integer PRIMARY KEY AUTOINCREMENT,
                            date datetime default (datetime('now','localtime')),
                            soil_moisture_pct integer
                        );"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def drop_table(conn, table_name):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    create_table_sql = f"""DROP TABLE IF EXISTS {table_name};"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_data(conn, table, data):
    """
    Create a new project into the projects table
    :param conn:
    :param table:
    :param data: tuple, plant data passed in as a tuple following the format
    (DATETIME, )
    :return: row id
    """
    sql = f''' INSERT INTO {table}(soil_moisture_pct)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, clean_data(data))
    conn.commit()
    return cur.lastrowid

if __name__ == "__main__":
    pass