import os
import sqlite3
import mock_data_sql
import operator
import matplotlib.


dbInfo = {} # db related info

def get_files(dir):
    # Get current working directory
    saved_path = os.getcwd()
    # Change directories to where the data is:
    os.chdir(dir)
    # Take only CSV files from the folder
    all_list = [f for f in os.listdir(dir) if f[-4:] == ".csv"]
    # List over files
    count = 1
    for data_file in all_list:
        with open(data_file, mode='rt', encoding='utf-8') as fd:
            for recline in fd:
                # Record Map Header:
                #  0   1      2      3    4     5         6
                # id,number,street,city,state,postalCode,price
                # Clean records from newlines
                rec = recline.strip().split(',')
                # Exclude header files
                if rec[0] == "id":
                    continue
                # Eliminate leading zeros from street Number
                rec[1] = int(rec[1])
                # Remove $ from price
                rec[6] = float(rec[6].replace("$",""))
                # Update counter to have a unique record Id
                rec[0] = count
                count += 1
                # Clean Record
                #print(rec)
                # Insert data
                mock_data_sql.dynamic_data_entry(dbInfo, rec)
                # Commit to DB every 100 records
                if rec[0] % 100 == 0:
                    dbInfo['con'].commit()

        # last commit
        dbInfo['con'].commit()
    # Change back to original dir
    os.chdir(saved_path)


def display_state_info(data):
    """

    :param data:
    :return:
    """
    state = {}

    for rec in data:
        if rec[4] in state:
            state[rec[4]] +=1
        else:
            state[rec[4]] = 1

    sname = []
    scount = []
    #s_state = sorted(state.items())
    for st, count in state.items():
        print(st, count)
        sname.append(st)
        scount.append(st)


    #print(s_state)



def main():
    # Connect to DB
    dbInfo['con'] = sqlite3.connect('tutorial.db')
    # Create a cursor (interact with DB)
    dbInfo['cur'] = dbInfo['con'].cursor()
    mock_data_sql.create_table(dbInfo)
    # Path to data
    data_dir = r"C:\Users\kitof\PycharmProjects\kitspython\data"
    #get_files(data_dir)
    data = mock_data_sql.read_data(dbInfo)
    # for rec in data:
    #     print(rec)
    display_state_info(data)

    dbInfo['cur'].close()
    dbInfo['con'].close()


if __name__ == '__main__':
    main()




