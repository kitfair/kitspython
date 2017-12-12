import sys

def sqrt(x):
    """
    Compute the square root
    :param x: The number to be square rooted
    :return: The square root
    :raise ValueError on DivisionByZero
    """


    guess = x
    i = 0
    try:
        while guess * guess != x and i<20:
            guess = (guess+ x/guess)/2.0
            i+= 1
    except ZeroDivisionError:
        raise ValueError()

    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(-1))
        print("This is never printed")
    except ValueError as e:
        print(e, file=sys.stderr)


    print("Program execution continues here")


if __name__ == '__main__':
    main()
