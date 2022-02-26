from matplotlib import pyplot as plt
import numpy as np

# the basis_data
x = 1990
y = 2006
year = np.arange(x, y, 2)
g1 = [2.6, 2.8, 2.5, 2.3, 1.9, 2.0, 1.8, 1.7]
g2 = [3.5, 3.0, 3.1, 2.9, 2.7, 2.8, 2.6, 2.5]
g3 = np.arange(2, 18, 2).tolist()
labels = ['g1', 'g2', 'g3']


# to generate vertical graph
def answer_one():
    plt.title("Average Yearly CGPA")
    plt.bar(year, g1, color="r", width=0.35)
    plt.bar(year + 0.35, g2, color="g", width=0.35)
    plt.bar(year + 0.7, g3, color="y", width=0.35)
    plt.show()


def answer_two():

    # diffGraph()
    # stackplot()
    xticks()
    # pie_line()
    # bars('v')
    # bars('r')
    # scatter()
    # plotting()
    # plot_line()
    # lineGraph()


def diffGraph():
    fig, (ax1) = plt.subplots(1, 1, sharex=True)
    ax1.set_title('interpolation=False')
    ax1.plot(year, g1, 'o--')
    ax1.plot(year, g2, 'o--')
    ax1.fill_between(year, g1, g2, color='C0', alpha=0.3)
    ax1.fill_between(year, g2, g3, color='C1', alpha=0.3)

    fig.tight_layout()
    plt.show()

def stackplot():
    plt.plot([], [], color='r', label='1', linewidth=5)
    plt.plot([], [], color='g', label='2', linewidth=5)
    plt.plot([], [], color='b', label='3', linewidth=5)
    plt.stackplot(year, g1, g2, g3, colors=['m', 'c', 'r'])
    plt.show()


def xticks():
    width = 0.5
    plt.bar(year, g1, width, color='red', label='g1')
    plt.bar(year, g2, width, bottom=g1, color='yellow', label='g2')
    plt.bar(year, g3, width, bottom=g2, color='gray', label='g3')
    plt.xticks(year + width / 2, year, rotation=40)
    plt.legend()
    plt.show()


def pie_line():
    plt.subplot(2, 2, 1)
    plt.pie(g1, labels=year)

    plt.subplot(2, 2, 2)
    plt.pie(g2, labels=year)

    plt.subplot(2, 2, 3)
    plt.pie(g3, labels=year)

    plt.subplot(2, 2, 4)
    plt.bar(year, g1, color="r", width=0.35)
    plt.bar(year + 0.35, g2, color="g", width=0.35)
    plt.bar(year + 0.7, g3, color="y", width=0.35)

    plt.show()


def bars(type):
    plt.title("Average Yearly CGPA")
    if (type == 'r'):
        plt.bar(year, g1, color="r", width=0.35)
        plt.bar(year + 0.35, g2, color="g", width=0.35)
        plt.bar(year + 0.7, g3, color="y", width=0.35)
    if (type == 'v'):
        plt.barh(year, g1, color="r", height=0.35)
        plt.barh(year + 0.35, g2, color="g", height=0.35)
        plt.barh(year + 0.7, g3, color="y", height=0.35)
    plt.show()


def scatter():
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, ])
    plt.scatter(year, g1, c=colors, cmap='viridis')
    plt.scatter(year, g2, c=colors[::-1], cmap='viridis')
    plt.scatter(year, g3, c='r', cmap='viridis')
    plt.colorbar()
    plt.show()


def plot_line():
    plt.plot(year, g1, 'o:r')
    plt.plot(year, g2, 'o:g')
    plt.plot(year, g3, 'o:y')
    plt.show()


def plotting():
    plt.plot(year, g1, 'o')
    plt.plot(year, g2, 'o')
    plt.plot(year, g3, 'o')
    plt.show()


def lineGraph():
    plt.plot(year, g1, )
    plt.plot(year, g2, )
    plt.plot(year, g3, )
    plt.show()


answer_two()
