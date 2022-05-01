import sqlite3
from sqlite3 import Error
from faker import Faker


def initialize_database(db_file='data.db'):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def load_data(conn, n=10):
    fake = Faker()

    for i in range(n):
        profile = fake.profile()
        prof = (profile['job'], profile['company'], profile['ssn'], profile['sex'], profile['name'], profile['birthdate'], profile['username'])
        create_profile(conn, prof)

def create_profile(conn, profile):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO profiles(job,company,ssn,sex,name,birthdate,username)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, profile)
    conn.commit()

    return cur.lastrowid

        


    


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("DROP TABLE IF EXISTS profiles")
        table = """ CREATE TABLE profiles (
            job VARCHAR(255) NOT NULL,
            company VARCHAR(255) NOT NULL,
            ssn VARCHAR(255) NOT NULL,
            sex VARCHAR(255) NOT NULL,
            name VARCHAR(255),
            birthdate VARCHAR(255),
            username VARCHAR(255)
        ); """
        conn.execute(table)
        load_data(conn, 1000)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection("data.db")

 