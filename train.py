from keras.models import Sequential
from keras.layers import Dense
import numpy as np
# fix random seed for reproducibility
np.random.seed(7)

def main():
	#load dataset
	dataset = np.loadtxt("data_train.csv", delimiter=",")
	X = dataset[:, 0:2]
	Y = dataset[:, 2]
	
	#Create model
	model = Sequential()
	model.add(Dense(12, input_dim=2, activation='relu'))
	model.add(Dense(8, activation='relu'))
	model.add(Dense(1, activation='sigmoid'))
	
	# Compile model
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	# Fit the model
	model.fit(X, Y, epochs=150, batch_size=10)
	
# 	dataset = np.loadtxt("data_test.csv", delimiter=",")
# 	X = dataset[:, 0:2]
# 	Y = dataset[:, 2]
	scores = model.evaluate(X, Y)
	print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
	model.save_weights('weights.h5')

main()
