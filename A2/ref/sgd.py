# USAGE
# python sgd.py

# import the necessary packages
import data
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
import numpy as np

learning_rate = 0.0001
batch_size = 1
epochs = 100000000

def sigmoid_activation(x):
	# compute and return the sigmoid activation value for a
	# given input value
	return 1.0 / (1 + np.exp(-x))

def next_batch(X, y, batchSize):
	# loop over our dataset `X` in mini-batches of size `batchSize`
	for i in np.arange(0, X.shape[0], batchSize):
		# yield a tuple of the current batched data and labels
		yield (X[i:i + batchSize], y[i:i + batchSize])


# generate a 2-class classification problem with 400 data points,
# where each data point is a 2D feature vector
X = data.perc_data()
y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# (X, y) = make_blobs(n_samples=4, n_features=2, centers=2,
# 	cluster_std=2.5, random_state=95)
print("X",X)
print("y",y)
#np.column_stack((lat, lon))

# insert a column of 1's as the first entry in the feature
# vector -- this is a little trick that allows us to treat
# the bias as a trainable parameter *within* the weight matrix
# rather than an entirely separate variable
X = np.c_[np.ones((X.shape[0])), X]


# initialize our weight matrix such it has the same number of
# columns as our input features
print("[INFO] starting training...")
W = np.random.uniform(size=(X.shape[1],))

# loop over the desired number of epochs
for epoch in range(100):

	# loop over our data in batches
	for (batchX, batchY) in next_batch(X, y, batch_size):
		# take the dot product between our current batch of
		# features and weight matrix `W`, then pass this value
		# through the sigmoid activation function
		preds = sigmoid_activation(batchX.dot(W))

		# now that we have our predictions, we need to determine
		# our `error`, which is the difference between our predictions
		# and the true values
		error = preds - batchY

		# the gradient update is therefore the dot product between
		# the transpose of our current batch and the error on the
		# # batch
		gradient = batchX.T.dot(error) / batchX.shape[0]

		# use the gradient computed on the current batch to take
		# a "step" in the correct direction
		W += -learning_rate * gradient

print("W", W)
# compute the line of best fit by setting the sigmoid function
# to 0 and solving for X2 in terms of X1
Y = (-W[0] - (W[1] * X)) / W[2]

#print("X HÄR",X)
# plot the original data along with our line of best fit
plt.figure()
plt.scatter(X[:, 1], X[:, 2], marker="o", c=y)
plt.plot(X, Y, "r-")
plt.show()