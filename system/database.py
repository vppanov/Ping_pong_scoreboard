import sqlite3
from sqlite3 import Error
import os


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


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    path2 = os.getcwd()
    full = os.path.join(path2, "system/stats.db")
    database = full

    sql_create_statistics_table = """ CREATE TABLE IF NOT EXISTS Singles_statistics (
                                        Match_id integer PRIMARY KEY,
                                        Player_1_Name text,
                                        Player_2_Name text,
                                        Player_1_Score integer,
                                        Player_2_Score integer,
                                        Match_duration text,
                                        Date text
                                    ); """
    sql_create_statistics_doubles_table = """ CREATE TABLE IF NOT EXISTS Doubles_statistics (
                                        Match_id integer PRIMARY KEY,
                                        Team_1_Name text,
                                        Team_2_Name text,
                                        Team_1_Score integer,
                                        Team_2_Score integer,
                                        Match_duration text,
                                        Date text
                                    ); """



    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_statistics_table)
        create_table(conn, sql_create_statistics_doubles_table)



    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
