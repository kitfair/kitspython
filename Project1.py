#Task is open a file from the web
#iterate over the file
#Create list of words
#Iterate over new list
"""
This is my first project which will be documented later
"""
from urllib.request import urlopen
import sys
def story_words(f):
    """
    Fetch a list of words from a file
    :param f: url address of a file
    :return: nothing
    """

    #f = "http://icarus.cs.weber.edu/~hvalle/hafb/wasteland.txt"
    with urlopen(f) as story:
        g = []
        for line in story:
            story_line = line.decode('utf-8').split()
            #print(line.decode('utf-8').split())
            for words in story_line:
                g.append(words)

    print("Length: ",len(g),"words")


def main(n):
    story_words(n)


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)






