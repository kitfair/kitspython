import sqlite3
import time
import datetime
import random


def create_table(dbInfo):
    """

    :param dbInfo:
    :return:
    """

    dbInfo['cur'].execute("""CREATE TABLE IF NOT EXISTS STUFF(unix REAL, datestamp TEXT, keyword TEXT, value REAL)""")

def data_entry(dbinfo):
    """

    :param dbinfo:
    :return:
    """
    dbinfo['cur'].execute("""INSERT INTO STUFF VALUES(123456789, '2017-12-14 10:11:30', 'Python', 5)""")
    dbinfo['con'].commit()

def read_data(dbinfo):
    """

    :param dbinfo:
    :return:
    """
    dbinfo['cur'].execute("""SELECT * FROM STUFF WHERE value = 4""")
    data = dbinfo['cur'].fetchall()
    for row in data:
        print(row)
def delete_data(dbinfo):
    """

    :param dbinfo:
    :return:
    """

    print("Before delete")
    dbinfo['cur'].execute("""SELECT * FROM STUFF""")
    data = dbinfo['cur'].fetchall()
    [print(row) for row in data]

    print("After delete")
    dbinfo['cur'].execute("""DELETE FROM STUFF WHERE value = 2""")
    dbinfo['cur'].execute("""SELECT * FROM STUFF""")
    data = dbinfo['cur'].fetchall()
    [print(row) for row in data]






def dynamic_data_entry(dbinfo):
    """

    :param dbinfo:
    :return:
    """

    unix = int(time.time())
    date = datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S")
    keyword = 'Python'
    value = random.randrange(0,10)
    dbinfo['cur'].execute("""INSERT INTO STUFF(unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)""",(unix, date, keyword, value))
    dbinfo['con'].commit()

def main():
    dbInfo = {}
    # connection
    dbInfo['con'] = sqlite3.connect('tutorial.db')
    #Cursor
    dbInfo['cur'] = dbInfo['con'].cursor()
    create_table(dbInfo)
    #insert data
    #data_entry(dbInfo)
    # for i in range(10):
    #     dynamic_data_entry(dbInfo)
    #     time.sleep(2)
    #read_data(dbInfo)
    delete_data(dbInfo)




    #clean
    dbInfo['cur'].close()
    dbInfo['con'].close()


if __name__ == '__main__':
    main()