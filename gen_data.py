'''
Generate data for y = 2x + 1
'''
import numpy as np
import csv

samples = 1000

def gen():
	file = open('data_train.csv', 'wt')
	writer = csv.writer(file)
	
	print "===class 0==="
	for i in range(samples/2):
		x = np.round(np.random.random_sample()*10,2)
		y = np.round(2*x + 1 + np.random.random_sample()*x,2)
		print x, '\t', y
		writer.writerow((str(x), str(y),'0'))
		
	print "\n===class 1==="
	for i in range(samples/2):
		x = np.round(np.random.random_sample()*10,2)
		y = np.round(2*x + 1 - np.random.random_sample()*x,2)
		print x, '\t', y
		writer.writerow((str(x), str(y), '1'))
		
	file.close()
gen()
