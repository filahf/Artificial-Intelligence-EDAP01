import data
import numpy as np
import random
import matplotlib.pyplot as plt


def col_of_ones(X):
    X = np.c_[np.ones((X.shape[0])), X]
    return X


def sgd(X, learning_rate, epochs):
    w0, w1, w2 = 1, 1, 1
    for i in range(epochs):
        row = random.choice(X)
        randConst = row[0]
        randX = row[1]
        randY = row[2]

        phi_w0 = 2 * (((w0 * 1) + (w1 * randX) + (w2 * randY)) * randConst)
        phi_w1 = 2 * (((w0 * 1) + (w1 * randX) + (w2 * randY)) * randX)
        phi_w2 = 2 * (((w0 * 1) + (w1 * randX) + (w2 * randY)) * randY)

        w0 -= learning_rate * phi_w0
        w1 -= learning_rate * phi_w1
        w2 -= learning_rate * phi_w2

    return w0, w1, w2


def main():
    learning_rate = 0.01
    epochs = 100000 
    chars_all, chars_a = data.load_data(
        "/home/filip/Documents/Artificial-Intelligence-EDAP01/A2/salammbo_a_en.tsv")
    X = np.column_stack((chars_all, chars_a))

    w0, w1, w2 = sgd(col_of_ones(X), learning_rate, epochs)

    x = np.linspace(0, 1, 100)
    Y = (-w0 - w1 * x) / w2

    plt.plot(x, Y)
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()


if __name__ == "__main__":
    main()
