from contextlib import closing

class RefridgeratorRaider:

    def openf(self):
        print("open fridge door")

    def takef(self, food):
        print("Finding {}.. ".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError('Health warning!')
        print("Taking {}".format(food))

    def raid(self,food):

        with closing(RefridgeratorRaider()) as r:

            r.openf()
            r.takef(food)
            r.closef()


    def closef(self):
        print('Close fridge door')
def raid(food):

    with closing(RefridgeratorRaider()) as r:

        r.openf()
        r.takef(food)
        r.closef()