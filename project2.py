from webbrowser import open as openw
import time


def my_break(break_info=None):
    """

    :param break_info: dictionary with following items
        t_break int
        url string
        t_sleep int
    :return:
    """
    if break_info is None:
        break_info = {}
        break_info["t_breaks"] = 3
        break_info["url"] = "https://www.youtube.com/watch?v=Q0CbN8sfihY"
        break_info["t_sleep"] = 60 *60

    break_count = 0


    while break_count < break_info(["t_breaks"]):

        time.sleep(break_info(["t_sleep"]))
        openw(break_info(["url"]))
        break_count += 1

if __name__ == '__main__':
    info = {}
    print('hello')
    my_break()
