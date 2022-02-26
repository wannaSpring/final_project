from matplotlib import pyplot as plt
import numpy as np

# the basis_data
x = 1990
y = 2006
year = np.arange(x, y, 2)
g1 = [2.6, 2.8, 2.5, 2.3, 1.9, 2.0, 1.8, 1.7]
g2 = [3.5, 3.0, 3.1, 2.9, 2.7, 2.8, 2.6, 2.5]
taylor_Uni = np.arange(2, 18, 2).tolist()
labels = ['g1', 'g2', 'taylor_Uni']


def answer_one():
    xList = np.arange(len(year))  # x轴刻度标签位置
    width = 0.25  # bar width
    plt.title("Average Yearly CGPA")
    plt.bar(xList - width, g1, width, label='1')
    plt.bar(xList, g2, width, label='2')
    plt.bar(xList + width, taylor_Uni, width, label='3')
    plt.xticks(xList, labels=year)
    plt.show()


def answer_two():
    diffGraph()
    stackplot()
    xticks()
    pie_line()
    bars('v')
    bars('r')
    scatter()
    plotting()
    plot_line()
    lineGraph()


def diffGraph():
    fig, (ax1) = plt.subplots(1, 1, sharex=True)
    ax1.set_title('interpolation=False')
    ax1.plot(year, g1, 'o--')
    ax1.plot(year, g2, 'o--')
    ax1.fill_between(year, g1, g2, color='C0', alpha=0.3)
    ax1.fill_between(year, g2, taylor_Uni, color='C1', alpha=0.3)
    fig.tight_layout()
    plt.legend(['g1', 'g2', 'taylor_Uni'])
    plt.show()


def stackplot():
    plt.plot([], [], color='r', label='1', linewidth=5)
    plt.plot([], [], color='g', label='2', linewidth=5)
    plt.plot([], [], color='b', label='3', linewidth=5)
    plt.stackplot(year, g1, g2, taylor_Uni, colors=['m', 'c', 'r'])
    plt.legend(['g1', 'g2', 'taylor_Uni'])
    plt.show()


def xticks():
    width = 0.5
    plt.bar(year, g1, width, color='red', label='g1')
    plt.bar(year, g2, width, bottom=g1, color='yellow', label='g2')
    plt.bar(year, taylor_Uni, width, bottom=g2, color='gray', label='taylor_Uni')
    plt.xticks(year + width / 2, year, rotation=40)
    plt.legend()
    plt.legend(['g1', 'g2', 'taylor_Uni'])
    plt.show()


def pie_line():
    plt.subplot(2, 2, 1)
    plt.pie(g1, labels=year)

    plt.subplot(2, 2, 2)
    plt.pie(g2, labels=year)

    plt.subplot(2, 2, 3)
    plt.pie(taylor_Uni, labels=year)

    plt.subplot(2, 2, 4)
    plt.bar(year, g1, color="r", width=0.35)
    plt.bar(year + 0.35, g2, color="g", width=0.35)
    plt.bar(year + 0.7, taylor_Uni, color="y", width=0.35)
    plt.legend(['g1', 'g2', 'taylor_Uni'])
    plt.show()


def bars(type):
    plt.title("Average Yearly CGPA")
    if (type == 'r'):
        plt.bar(year, g1, color="r", width=0.35)
        plt.bar(year + 0.35, g2, color="g", width=0.35)
        plt.bar(year + 0.7, taylor_Uni, color="y", width=0.35)
    if (type == 'v'):
        plt.barh(year, g1, color="r", height=0.35)
        plt.barh(year + 0.35, g2, color="g", height=0.35)
        plt.barh(year + 0.7, taylor_Uni, color="y", height=0.35)
    plt.legend(['g1', 'g2', 'taylor_Uni'])
    plt.show()


def scatter():
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, ])
    plt.scatter(year, g1, c=colors, cmap='viridis')
    plt.scatter(year, g2, c=colors[::-1], cmap='viridis')
    plt.scatter(year, taylor_Uni, c='r', cmap='viridis')
    plt.colorbar()
    plt.legend(['g1', 'g2', 'taylor_Uni'])
    plt.show()


def plot_line():
    plt.plot(year, g1, 'o:r')
    plt.plot(year, g2, 'o:g')
    plt.plot(year, taylor_Uni, 'o:y')
    plt.legend(['g1', 'g2', 'taylor_Uni'])
    plt.show()


def plotting():
    plt.plot(year, g1, 'o')
    plt.plot(year, g2, 'o')
    plt.plot(year, taylor_Uni, 'o')
    plt.legend(['g1', 'g2', 'taylor_Uni'])
    plt.show()


def lineGraph():
    plt.plot(year, g1, )
    plt.plot(year, g2, )
    plt.plot(year, taylor_Uni, )
    plt.legend(['g1', 'g2', 'taylor_Uni'])
    plt.show()


# answer_one()
answer_two()
