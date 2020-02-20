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

def predict(weights, input):
    sum = np.dot(input,weights[1:]) + weights[0]
    #print("sum",sum)
    if sum > 0:
        return 1
    else:
        return -1

def train(training_set,labels,learning_rate,epochs):
    weights = np.zeros(3)
    for i in range(epochs):
        for inputs, label in zip(training_set,labels):
            prediction = predict(weights,inputs)
            weights[1] += learning_rate * (label - prediction) * inputs[0]
            weights[2] += learning_rate * (label - prediction) * inputs[1]
            weights[0] += learning_rate * (label - prediction)
    return weights


def main():
    epochs = 21050
    learning_rate = 0.01
    data, labels = libsvm_reader("A2/libsvm_data.libsvm")
    training_weights = train(data,labels,learning_rate,epochs)
    arr = [0.43217276, 0.43375984]
    print(predict(training_weights,arr))
    x = np.linspace(0, 1, 100)
    Y = (-training_weights[1] - training_weights[1] * x) / training_weights[1]
    #fixa scatter chart



if __name__ == "__main__":
    main()