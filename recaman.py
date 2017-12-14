import sys
from itertools import count, islice

def sequence():
    """

    :return: nothing
    """

    seen = set()
    a = 0
    for n in count(1) :
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c

def write_sequence(filename, num):
    """

    :param filename:
    :param num:
    :return:
    """

    f = open(filename, mode='wt', encoding='utf-8')
    f.writelines('{0}\n'.format(r) for r in islice(sequence(), num+1))
    f.close()

def read_series_with_block(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]
    # series = []
    # for line in f:
    #     #print(type(line))
    #     a = int(line.strip())
    #     series.append(a)
    # f.close()
    # return series

def words_per_line(flo):
    return [len(line.split()) for line in flo.readlines()]

def main():
    with open('test.txt', mode='rt', encoding='utf-8') as rf:
        wpl = words_per_line(rf)
    print(wpl, type(rf))
    # f = "recamanSeries.txt"
    # n = 100
    # write_sequence(f,n)
    # s = read_series_with_block(f)
    # print(s)

if __name__ == '__main__':
    main()