#16IE10002	
#Aditya Rathore
#Assignment 3
#python 16IE10002_3.py

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
			row[i] = int(row[i])
		data.append(row)
	data=np.array(data)
	X=data[:,:8]
	if y_flag:
		Y=data[:,8]
		return X,Y
	else:
		return X

def train(X,Y,Y1,Y0,P_yes,P_no):
	for i in range(X.shape[1]):
		for j in range(X.shape[0]):
			if X[j][i]==0:
				if Y[j] == 0:
					P_no[i][0] += 1
				else:
					P_no[i][1] +=1
			else:
				if Y[j] == 0:
					P_yes[i][0] +=1
				else:
					P_yes[i][1] +=1
		P_no[i][0] /= (Y0 + 2)
		P_no[i][1] /= (Y1 + 2)
		P_yes[i][0] /= (Y0 + 2)
		P_yes[i][1] /= (Y1 + 2)

def main():
	X,Y = get_data("data3.csv",1)
	Y1 = np.count_nonzero(Y)
	Y0 = Y.shape[0] - np.count_nonzero(Y)
	P_yes = np.ones([X.shape[1],2],dtype=np.float32)
	P_no = np.ones([X.shape[1],2],dtype=np.float32)
	
	train(X,Y,Y1,Y0,P_yes,P_no)

	X = get_data("test3.csv",0)
	for i in range(X.shape[0]):
		P0 = Y0
		P1 = Y1
		for j in range(X.shape[1]):
			if X[i][j] == 0:
				P0 *= P_no[j][0]
				P1 *= P_no[j][1]
			else:
				P0 *= P_yes[j][0]
				P1 *= P_yes[j][1]
		if P1 > P0 :
			print(1,end=" ")
		else :
			print(0,end=" ")
	print()

main()