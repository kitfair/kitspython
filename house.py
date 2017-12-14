
import os

def get_files(dir):
    file_list = os.listdir(dir)
    print(file_list)




def main():
    data_dir = r"C:\Users\kitof\PycharmProjects\kitspython\data"
    get_files(data_dir)

if __name__ == '__main__':
    main()