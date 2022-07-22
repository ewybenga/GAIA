"""
Support functions for communicating with sql from 
 - https://www.sqlitetutorial.net/sqlite-python/creating-tables/
 - https://www.sqlitetutorial.net/sqlite-python/insert/
"""
import sqlite3
from sqlite3 import Error

def clean_data(raw_data):
    #TODO: clean data based on config
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


def create_table(conn, table, clean=False):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    table_name = table["name"]
    table_cols = table["cols"]

    if clean:
        drop_table(conn, table_name)
    
    sql_cmd = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    date datetime default (datetime('now','localtime'))"""
    for val_name in table_cols:
        sql_cmd += f",\n{val_name} {table_cols[val_name]}"  # pulls the column names and types from the config file
    sql_cmd += ");"

    try:
        c = conn.cursor()
        c.execute(sql_cmd)
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
    # TODO: add config based data insert
    sql = f''' INSERT INTO {table}(soil_moisture_pct)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, clean_data(data))
    conn.commit()
    return cur.lastrowid

if __name__ == "__main__":
    pass