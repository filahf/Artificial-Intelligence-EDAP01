import data
import numpy as np
import random
import matplotlib.pyplot as plt


def bgd(X, y, learning_rate, epochs):
    w0, w1, w2 = 1, 1, 1
    phi_w0,phi_w1,phi_w2 = 1,1,1
    m = len(X)
    for iters in range(epochs):
        for i in range(m):
            phi_w0 += 2 * (((w0) + (w1 * X[i]) + (w2 * y[i])))
            phi_w1 += 2 * (((w0) + (w1 * X[i]) + (w2 * y[i])) * X[i])
            phi_w2 += 2 * (((w0) + (w1 * X[i]) + (w2 * y[i])) * y[i])
        phi_w0 = phi_w0/m
        phi_w1 = phi_w1/m
        phi_w2 = phi_w2/m

        w0 -= learning_rate * phi_w0
        w1 -= learning_rate * phi_w1
        w2 -= learning_rate * phi_w2
    return w0,w1,w2

def sgd(X, y, learning_rate, epochs):
    w0, w1, w2 = 1, 1, 1
    m = len(X)
    for iters in range(epochs):
        rand_ind = np.random.randint(0, m)
        x_i = X[rand_ind]
        y_i = y[rand_ind]

        phi_w0 = 2 * (((w0 * 1) + (w1 * x_i) + (w2 * y_i)))
        phi_w1 = 2 * (((w0 * 1) + (w1 * x_i) + (w2 * y_i)) * x_i)
        phi_w2 = 2 * (((w0 * 1) + (w1 * x_i) + (w2 * y_i)) * y_i)

        w0 -= learning_rate * phi_w0
        w1 -= learning_rate * phi_w1
        w2 -= learning_rate * phi_w2

    return w0, w1, w2


def perform_sgd(chars_all, chars_a, learning_rate, epochs):
    w0, w1, w2 = sgd(chars_all, chars_a, learning_rate, epochs)
    print("w0", w0)
    print("w1", w1)
    print("w2", w2)

    x = np.linspace(0, 1, 100)
    Y = (-w0 - w1 * x) / w2

    plt.plot(x, Y, label="Regression line")
    plt.legend(ncol=2, loc='upper left')
    plt.suptitle('Linear Regression SGD')
    plt.xlabel('Characters')
    plt.ylabel("Occurences of a")
    plt.scatter(chars_all, chars_a)
    plt.savefig('SGD_result.png')
    plt.show()


def perform_bgd(chars_all, chars_a, learning_rate, epochs):
    w0, w1, w2 = bgd(chars_all, chars_a, learning_rate, epochs)
    print("w0", w0)
    print("w1", w1)
    print("w2", w2)
    x = np.linspace(0, 1, 100)
    Y = (-w0 - w1 * x) / w2

    plt.plot(x, Y, label="Regression line")
    plt.scatter(chars_all, chars_a)
    plt.legend(ncol=2, loc='upper left')
    plt.suptitle('Linear Regression BGD')
    plt.xlabel('Characters')
    plt.ylabel("Occurences of a")
    plt.savefig('BGD_result.png')
    plt.show()


def main():
    learning_rate = 0.01
    epochs = 100000
    chars_all, chars_a = data.load_data(
        "A2/salammbo_a_en.tsv")
    #perform_sgd(chars_all, chars_a, learning_rate, epochs)
    perform_bgd(chars_all, chars_a,learning_rate,epochs)


if __name__ == "__main__":
    main()
