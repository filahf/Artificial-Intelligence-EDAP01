import data
import numpy as np
import random
import matplotlib.pyplot as plt


def col_of_ones(X):
    X = np.c_[np.ones((X.shape[0])), X]
    return X


def bgd(X, y, learning_rate, epochs, batch_size):
    w0, w1, w2 = 1, 1, 1
    #weights = np.ones(3)
    m = len(X)
    for iters in range(epochs):
        indices = np.random.permutation(m)
        X = X[indices]
        y = y[indices]
        for i in range(0, m, batch_size):
            X_i = X[i:i+batch_size]
            y_i = y[i:i+batch_size]
            phi_w0 = 2 * (((w0 * 1) + (w1 * X_i) + (w2 * y_i)))
            phi_w1 = 2 * (((w0 * 1) + (w1 * X_i) + (w2 * y_i)) * X_i)
            phi_w2 = 2 * (((w0 * 1) + (w1 * X_i) + (w2 * y_i)) * y_i)

            w0 -= learning_rate * phi_w0
            w1 -= learning_rate * phi_w1
            w2 -= learning_rate * phi_w2
    return np.mean(w0), np.mean(w1), np.mean(w2)


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


def perform_bgd(chars_all, chars_a, learning_rate, epochs, batch_size):
    w0, w1, w2 = bgd(chars_all, chars_a, learning_rate, epochs, batch_size)
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
    batch_size = 5
    learning_rate = 0.01
    epochs = 100000
    chars_all, chars_a = data.load_data(
        "/home/filip/Documents/Artificial-Intelligence-EDAP01/A2/salammbo_a_en.tsv")
    #perform_sgd(chars_all, chars_a, learning_rate, epochs)
    perform_bgd(chars_all, chars_a,learning_rate,epochs,batch_size)


if __name__ == "__main__":
    main()
