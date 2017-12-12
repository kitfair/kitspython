
import sys
from math import log

def convert(s):
    """
    convert to int
    :param s:  object to convert
    :return: integer object
    :raise: ValueError, TypeError
    """

    try:
        return int(s)

        #print("Conversion succeeded x = ", x)
    except (ValueError, TypeError) as e:
        print("Conversion failed: {}".format((str(e)),file=sys.stderr))
        #print("Conversion failed")
        raise #re-raising the error


def string_log(s):
    try:
        v = convert (s)
        return log(v)
    except (ValueError):
        print("Log conversion failed")

    return -1

def main():
    # i = convert("55")
    # print(i)
    # i = convert("Hello")
    # print(i)
    # i= convert([1,2,3])
    # print(i)
    i = string_log("55")
    print(i)
    i = string_log("hello")
    print(i)





if __name__ == '__main__':
    main()