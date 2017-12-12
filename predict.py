from keras.models import Sequential
from keras.layers import Dense
import numpy as np
# fix random seed for reproducibility
np.random.seed(7)

def main():
    #Create model
    model = Sequential()
    model.add(Dense(12, input_dim=2, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    #load model
    model.load_weights('weights.h5')
    
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    #load test dataset
    dataset = np.loadtxt("data_test.csv", delimiter=",")
    X = dataset[:, 0:2]
    Y = dataset[:, 2]
    
#     predictions = model.predict(X, batch_size=10, verbose=0)
#     
#     rounded = [round(x[0]) for x in predictions]
#     correct = 0
#     for i in range(100):
#         if(Y[i] == rounded[i]):
#             correct +=1
#     print "Accuracy:",correct*1.0/100
    
    scores = model.evaluate(X, Y)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

main()