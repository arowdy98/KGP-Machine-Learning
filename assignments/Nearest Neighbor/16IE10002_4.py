# 16IE10002
# Aditya Rathore
# Assignment 4
# python 16IE10002_4.py


import numpy as np

def get_data(filename,y_flag):
	data = []  #to store training data from csv file
	data_str = []

	with open(filename,"r") as csv_data:
		data_str = csv_data.read().split('\n')
	#print(len(data_str))
	
	for i in range(len(data_str)-1):	
		row = data_str[i].split(',')
		for i in range(len(row)):
			row[i] = float(row[i])
		data.append(row)
	data=np.array(data)
	X=data[:,:4]
	if y_flag:
		Y=data[:,4]
		return X,Y
	else:
		return X

X,Y = get_data("data4.csv",1)

X_t = get_data("test4.csv",0)
y_out = ""

def euclideanDistance(sample, train):
    distance = np.sum(np.square(sample - train))    
    # print(np.sqrt(distance))
    return np.sqrt(distance)


for i in range(X_t.shape[0]):
	difference = []
	least = np.zeros((5,2))

	count = 0
	for j in range(X.shape[0]):
		dist = euclideanDistance(X_t[i,:], X[j,:])
		difference.append(dist)
  			
	for x in range(5):
		d_min = 9999
		for a in range(len(difference)):
			if difference[a]<d_min:
				d_min = difference[a]
				index = a
		del difference[index]
		least[x, 0]= d_min
		least[x, 1]= Y[index]

		if Y[index] == 0:
			count += 1
		else:
			count -= 1

	if count > 0:
		y_out += str(0) + " "
	else :
		y_out += str(1) + " "	

print(y_out)
f = open("16IE10002_4.out",'w')
f.write(y_out)
f.close()