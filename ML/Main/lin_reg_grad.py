from matplotlib import pyplot as plt
import numpy as np

x_points = [0.20688998, 0.24651684, 0.08791665, 0.20467496, 0.17279488, 0.23341806,
            0.43217276, 0.21723448, 0.17992702, 0.14405179, 0.20974284, 0.22934172,
            0.42065117, 0.43692752, 0.1045525]
y_points = [0.20013435, 0.24924265, 0.08936987, 0.20527989, 0.1683584,  0.23525039,
            0.43375984, 0.21629315, 0.17991329, 0.14687352, 0.21439742, 0.23109785,
            0.41498314, 0.43971783, 0.10101504]

learn = .001  # .001, .01, .1, 1 ...
precision = 0.000001
step = 1
iters = 0
# y = mx + b
m = 0
b = 0


def y(x): return m*x + b


def plot_line(y, data_points):
    x_values = [i for i in range(
        int(min(data_points))-1, int(max(data_points))+2)]
    y_values = [y(x) for x in x_values]
    plt.plot(x_values, y_values, 'r')


def summation(y, x_points, y_points):
    total1 = 0
    total2 = 0
    for i in range(1, len(x_points)):
        total1 += y(x_points[i]) - y_points[i]
        total2 += (y(x_points[i]) - y_points[i]) * x_points[i]

    return total1 / len(x_points), total2 / len(x_points)


while step > precision:
    prev_m = m
    s1, s2 = summation(y, x_points, y_points)
    m = m - learn * s2
    b = b - learn * s1
    iters = iters+1
    step = abs(m - prev_m)

print(iters)
plot_line(y, x_points)
plt.plot(x_points, y_points, 'bo')
plt.show()