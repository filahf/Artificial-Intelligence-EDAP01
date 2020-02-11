from matplotlib import pyplot as plt

x_points = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y_points = [1, 2, 3, 1, 4, 5, 6, 4, 7, 10, 15, 9]


# y = mx + b
m = 0
b = 0


def y(x): return m*x + b


def plot_line(y, data_points):
    x_values = [i for i in range(
        int(min(data_points))-1, int(max(data_points))+2)]
    y_values = [y(x) for x in x_values]
    plt.plot(x_values, y_values, 'r')


learn = .001  # .001, .01, .1, 1 ...


def summation(y, x_points, y_points):
    total1 = 0
    total2 = 0

    for i in range(1, len(x_points)):
        total1 += y(x_points[i]) - y_points[i]
        total2 += (y(x_points[i]) - y_points[i]) * x_points[i]

    return total1 / len(x_points), total2 / len(x_points)


for i in range(1000):
    s1, s2 = summation(y, x_points, y_points)
    m = m - learn * s2
    b = b - learn * s1

plot_line(y, x_points)
plt.plot(x_points, y_points, 'bo')
plt.show()
