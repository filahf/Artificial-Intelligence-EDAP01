import data
import numpy as np
import random
import matplotlib.pyplot as plt


def col_of_ones(X):
    X = np.c_[np.ones((X.shape[0])), X]
    return X

def next_batch(X, batchSize):
	# loop over our dataset `X` in mini-batches of size `batchSize`
	for i in np.arange(0, X.shape[0], batchSize):
		# yield a tuple of the current batched data and labels
		yield (X[i:i + batchSize])

def bgd(X,y, learning_rate, epochs, batch_size):
    w0, w1, w2 = 1, 1, 1
    m = len(X)
    for iters in range(epochs):
        indices = np.random.permutation(m)
        X = X[indices]
        y = y[indices]
        for i in range(0,m,batch_size):
            X_i = X[i:i+batch_size]
            y_i = y[i:i+batch_size]
            const = 1
            phi_w0 = 2 * (((w0 * 1) + (w1 * X_i) + (w2 * y_i)) * const)
            phi_w1 = 2 * (((w0 * 1) + (w1 * X_i) + (w2 * y_i)) * X_i)
            phi_w2 = 2 * (((w0 * 1) + (w1 * X_i) + (w2 * y_i)) * y_i)

            w0 -= learning_rate * phi_w0
            w1 -= learning_rate * phi_w1
            w2 -= learning_rate * phi_w2
    return w0, w1, w2


    

def sgd(X, learning_rate, epochs):
    w0, w1, w2 = 1, 1, 1
    for iters in range(epochs):
        row = random.choice(X)
        const = row[0]
        x_i = row[1]
        y_i = row[2]

        phi_w0 = 2 * (((w0 * 1) + (w1 * x_i) + (w2 * y_i)) * const)
        phi_w1 = 2 * (((w0 * 1) + (w1 * x_i) + (w2 * y_i)) * x_i)
        phi_w2 = 2 * (((w0 * 1) + (w1 * x_i) + (w2 * y_i)) * y_i)

        w0 -= learning_rate * phi_w0
        w1 -= learning_rate * phi_w1
        w2 -= learning_rate * phi_w2

    return w0, w1, w2

def perform_sgd():
    learning_rate = 0.01
    epochs = 100000 
    chars_all, chars_a = data.load_data(
        "/home/filip/Documents/Artificial-Intelligence-EDAP01/A2/salammbo_a_en.tsv")
    X = np.column_stack((chars_all, chars_a))
    w0, w1, w2 = sgd(col_of_ones(X), learning_rate, epochs)
    print("w0",w0)
    print("w1",w1)
    print("w2",w2)

    x = np.linspace(0, 1, 100)
    Y = (-w0 - w1 * x) / w2
    
    plt.plot(x, Y)
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()

def perform_bgd():
    learning_rate = 0.01
    epochs = 100000 
    chars_all, chars_a = data.load_data(
        "/home/filip/Documents/Artificial-Intelligence-EDAP01/A2/salammbo_a_en.tsv")

    w0, w1, w2 = bgd(chars_all, chars_a, learning_rate, epochs,2)
    print("w0",w0)
    print("w1",w1)
    print("w2",w2)
    x = np.linspace(0, 1, 100)
    Y = (-w0[1] - w1[1] * x) / w2[1]
    
    plt.plot(x, Y)
    plt.scatter(chars_all, chars_a )
    plt.show()



def main():
    #perform_sgd()
    perform_bgd()


if __name__ == "__main__":
    main()
