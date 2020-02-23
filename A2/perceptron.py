import numpy as np
import matplotlib.pyplot as plt


def libsvm_reader(file):
    data = []
    labels = []
    with open(file) as f:
        for line in f:
            rows = line.strip().split()
            labels.append(int(rows[0]))
            data.append([float(rows[1]), float(rows[2])])
    return data, labels


def predict(weights, input, logistic):
    if(logistic):
        exponent = np.dot(input, weights[1:]) + weights[0]
        return 1.0 / (1 + np.exp(-exponent))
    else:
        sum = np.dot(input, weights[1:]) + weights[0]
        if sum > 0:
            return 1
        else:
            return 0


def train(training_set, labels, learning_rate, epochs, logistic = False):
    weights = np.zeros(3)
    for i in range(epochs):
        for inputs, label in zip(training_set, labels):
            prediction = predict(weights, inputs, logistic)

            weights[1] += learning_rate * (label - prediction) * inputs[0]
            weights[2] += learning_rate * (label - prediction) * inputs[1]
            weights[0] += learning_rate * (label - prediction)
    return weights

def cross_validate(data,labels,epochs,learning_rate,logistic):
    correct_guess = 0
    i = 1
    for i in range(30):
        train_data = data.copy()
        train_labels = labels.copy()
        del train_data[i]
        del train_labels[i]
        sample = data[i]
        weights = train(train_data,train_labels,learning_rate,epochs,logistic)
        print(predict(weights,np.array(sample),logistic))
        if (predict(weights,np.array(sample),logistic) == labels[i]):
            correct_guess += 1
    print(correct_guess/30)
    return correct_guess / 30




def main():
    # ---------ARGS--------------------------
    epochs = 10000
    learning_rate = 0.01
    data, labels = libsvm_reader("A2/libsvm_data_unscaled.libsvm")

    # ------------PERCE-------------
    #training_weights = train(data, labels, learning_rate, epochs)
    #print("Weights", training_weights)
    #print(data)
    #arr = np.array([75352,4871])
    #print("predicted", predict(training_weights, arr, False))

    cross_validate(data,labels,epochs,learning_rate,True)

    # --------PLOT----------------
    # x = np.linspace(0, 85000, 10000000)
    # Y = (-training_weights[0] - training_weights[1] * x) / training_weights[2]
    # chars = [i[0] for i in data]
    # chars_a = [i[1] for i in data]
    # plt.scatter(chars, chars_a, c=labels)
    # plt.plot(x, Y)
    # plt.show()


if __name__ == "__main__":
    main()
