
def swap(val):
    """

    :param val: a list of object
    :return: new order list
    """
    m = len(val)//2
    return val[m:]+val[:m]



def main():
    val = [9,13,21,4,11,7,1,3]
    print(val)
    val = swap(val)
    print(val)


if __name__ == '__main__':
    main()