"""
Object model test scripts
from ObjectModel import number_info
"""
import math

def modify(k):
    """
    Modifies the content of my list
    :param k: list
    :return: mothing
    """
    k.append(33)
    print('k=', k)


def replace(g):
    """

    Replace contents of list
    :param g: list object
    :return: nothing
    """

    g = [17, 36, 22, 33]
    print("g=", g)


def update_info(h):
    """
    increments each member by one
    :param h: List object
    :return:
    """
    for member in h:
        member = member + 10
def banner(message, border='*'):
    """
    Displays message surrounded by boarded
    :param message:message string
    :param border: border style(char)
    :return: nothing

    """

    print(border*(len(message)+4))

    print(border,message,border)
    print(border * (len(message)+4))






def main():
    m = [9, 12, 45]
    print("Before", m)
    modify(m)
    print(m)
    replace(m)
    print("After replace=", m)
    update_info(m)
    print('after update=',m)
    banner("hello","*")
    banner("", "#")
    banner("hello")

    #When are default arguments evaluated??

def add_spam(menu=None):
    """
    Add spam to my list
    :param menu: Optional list object
    :return: menu
    """
    if menu is None:
        menu = []
    menu.append("spam")
    return menu

def number_info():
    """
    function that prompts user for two ints and prints the sum the difference the product the average and the distance the max and min

    :return:
    """
    print("Enter first number:")
    num1 = int(input())
    print("Enter second number:")
    num2 = int(input())

    print('Sum= ',num1+num2)
    print('Difference= ',num1-num2)
    print('product=',num1*num2)
    print('average=',(num1+num2)/2)
    print('Distance=', abs(num1-num2))
    print('Max=',max(num1,num2))
    print('Min=',min(num1, num2))

if __name__ == '__main__':
    #main()
    number_info()
