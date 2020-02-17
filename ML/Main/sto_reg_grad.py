#b = b - learning_rate * error * x
import numpy as np

x_points = [0.20688998, 0.24651684, 0.08791665, 0.20467496, 0.17279488, 0.23341806,
            0.43217276, 0.21723448, 0.17992702, 0.14405179, 0.20974284, 0.22934172,
            0.42065117, 0.43692752, 0.1045525]
y_points = [0.20013435, 0.24924265, 0.08936987, 0.20527989, 0.1683584,  0.23525039,
            0.43375984, 0.21629315, 0.17991329, 0.14687352, 0.21439742, 0.23109785,
            0.41498314, 0.43971783, 0.10101504]
def data(x_points,y_points):
	return np.column_stack((x_points,y_points))

def predict(row, coefficients):
    yhat = coefficients[0]
    for i in range(len(row)-1):
        yhat += coefficients[i + 1] * row[i]
    return yhat

# Estimate linear regression coefficients using stochastic gradient descent


def coefficients_sgd(data, l_rate, n_epoch):
    coef = [0.0 for i in range(len(data[0]))]  # Längden på x array
    for epoch in range(n_epoch):
        sum_error = 0
        for row in data:
            yhat = predict(row, coef)
            error = yhat - row[-1]
            sum_error += error**2
            coef[0] = coef[0] - l_rate * error
            for i in range(len(row)-1):
                coef[i + 1] = coef[i + 1] - l_rate * error * row[i]
        #print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return coef


# Calculate coefficients
l_rate = 0.001
n_epoch = 1000
coef = coefficients_sgd(data(x_points,y_points), l_rate, n_epoch)
print(coef)