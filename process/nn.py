from analyze import processData

import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import operator
import tensorflow as tf
import pylab as plt



learning_rate = 10e-5
epochs = 1000
batch_size = 32
num_neuron = 30
seed = 10
beta = 10e-3
np.random.seed(seed)

data2 = "test2.csv"
df = pd.read_csv(data2)
df = df.dropna(axis=1)
df.head()


dataArray = df.values
resultArray = []

types = ['growth', 'confidence', 'strategic', 'productive', 'team']


prediction = []
for data in dataArray:

	datadict = {}
	for index, value in enumerate(data):
		datadict[index+1] = value
	result = processData(datadict, collaborate = False)

	prediction.append([result[type] for type in types])

NUM_FEATURES = 40

dataArray = np.delete(dataArray, list(range(0, dataArray.shape[1], 2)), axis=1)

dataArray = np.asmatrix(dataArray)
prediction = np.asmatrix(prediction)

print(dataArray.shape)
print(prediction.shape)

print(dataArray)
print(prediction)
m = 3* dataArray.shape[0] // 10

testX, testY =  dataArray[:m], prediction[:m]
trainX, trainY = dataArray[m:], prediction[m:]

trainX = (trainX- np.mean(trainX, axis=0))/ np.std(trainX, axis=0)
testX = (testX- np.mean(testX, axis=0))/ np.std(testX, axis=0)



# Create the model
x = tf.placeholder(tf.float32, [None, NUM_FEATURES])
y_ = tf.placeholder(tf.float32, [None, 5])

#build hidden layer of 30 neurons w Relu
weights_1 = tf.Variable(tf.truncated_normal([NUM_FEATURES, num_neuron], stddev=1.0 / np.sqrt(NUM_FEATURES), dtype=tf.float32), name='weights_1')
biases_1 = tf.Variable(tf.zeros([num_neuron]), dtype=tf.float32, name='biases_1')
u_1 = tf.add(tf.matmul(x, weights_1), biases_1)
output_1 = tf.nn.relu(u_1)

weights_2 = tf.Variable(tf.truncated_normal([num_neuron, num_neuron], stddev=1.0 / np.sqrt(num_neuron), dtype=tf.float32), name='weights_1')
biases_2 = tf.Variable(tf.zeros([num_neuron]), dtype=tf.float32, name='biases_1')
u_2 = tf.add(tf.matmul(output_1, weights_2), biases_2)
output_2 = tf.nn.relu(u_2)

weights_3 = tf.Variable(tf.truncated_normal([num_neuron, num_neuron], stddev=1.0 / np.sqrt(num_neuron), dtype=tf.float32), name='weights_1')
biases_3 = tf.Variable(tf.zeros([num_neuron]), dtype=tf.float32, name='biases_1')
u_3 = tf.add(tf.matmul(output_2, weights_3), biases_3)
output_3 = tf.nn.relu(u_3)

#final output layer
weights_4 = tf.Variable(tf.truncated_normal([num_neuron, 5], stddev=1.0 / np.sqrt(num_neuron), dtype=tf.float32), name='weights_2')
biases_4 = tf.Variable(tf.zeros([5]), dtype=tf.float32, name='biases_2')
y = tf.matmul(output_3, weights_4) + biases_4


reg_loss = tf.nn.l2_loss(weights_1) + tf.nn.l2_loss(weights_2)
reg_loss = reg_loss*beta
loss = tf.reduce_mean(tf.square(y_ - y))  + reg_loss

#Create the gradient descent optimizer with the given learning rate.
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train_op = optimizer.minimize(loss)
error = tf.reduce_mean(tf.square(y_ - y))
train_err = []
test_errors = []
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())

	for i in range(epochs):
		#batch gradient descent
		for start, end in zip(range(0, trainX.shape[0], batch_size), range(batch_size, trainX.shape[0], batch_size)):
			train_op.run(feed_dict={x: trainX[start:end], y_: trainY[start:end]})


		err = error.eval(feed_dict={x: trainX, y_: trainY})
		train_err.append(err)

		if i % 100 == 0:
			print('iter %d: validation error %g'%(i, train_err[i]))
		err = error.eval(feed_dict={x: testX, y_: testY})


		test_errors.append(err)

	predictions = sess.run(y,{ x: testX})



print("final error",test_errors[-1])
# plot learning curves
plt.figure(1)
plt.plot(range(epochs), train_err)
plt.xlabel(str(epochs) + ' iterations')
plt.ylabel('Train Error')

plt.figure(2)
plt.plot(range(epochs),test_errors)
plt.xlabel(str(epochs) + ' iterations')
plt.ylabel('Test Error')

truth = np.squeeze(np.asarray(testY))

truth = [a[0] for a in truth]
pred = [a[0] for a in predictions]
print("truth",truth)
print("pred",pred)
list1, list2 = (list(t) for t in zip(*sorted(zip(truth,pred))))

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]



correct = 0
for a , b in zip(list1,list2):
	if a == b or abs(a-b)<=1:
		correct += 1

print("predicted correctly +- 1 ", correct, " out of ", len(list1) )

plt.figure(3)
plt.plot(range(len(list1)), list1,'ro')
plt.plot(range(len(list1)), list2,'bo')
plt.xlabel('Red = Truth, Blue = Predictions')
plt.ylabel('Prediction')
plt.show()

plt.show()
