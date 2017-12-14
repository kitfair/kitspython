import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
axl = fig.add_subplot(1,1,1)


def animate(i):
    with open("ani_data.txt", mode='rt', encoding='utf-8') as gd:

        xs = []
        ys = []
        for line in gd:
            x, y = line.split(',')
            xs.append(int(x))
            ys.append(int(y))

    axl.clear()
    axl.plot(xs,ys)
ani = animation.FuncAnimation(fig)
