'''
Roll no. 16IE10002
Name: Aditya Rathore
Assignment: 2
Instructions: python3 16IE10002_2.py
'''
import numpy as np
import math

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def entropy(m,n):
	if(m == 0 or n == 0):
		return 0
	else:
		return -(m/(m + n))*math.log((m/(m + n)), 2) -(n/(m + n))*math.log((n/(m + n)), 2)

def total_entropy(X,Y):
	m=n=0.0
	for i in range(X.shape[0]):
		if(Y[i]==1):
			m+=1
		else:
			n+=1
	return entropy(m,n)

def get_max(X,Y,Et,lookup):
	max_g = -1
	max_i = -1
	for i in range(X.shape[1]):
		if i in lookup :
			continue
		m1=n1=m2=n2=p=n=0.0
		for j in range(X.shape[0]):
			if X[j][i] == 0:
				n+=1
				if Y[j]==1 :
					m1+=1
				else:
					n1 +=1
			else:
				p+=1
				if Y[j]==1 :
					m2+=1
				else:
					n2+=1
		E_neg = entropy(m1,n1)
		E_pos = entropy(m2,n2)
		G= (p*E_pos + n*E_neg)/(p+n)
		G= Et-G
		if max_g < G :
			max_g=G
			max_i=i
	return max_i

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

def train(X,Y,lookup):
	if(len(lookup) == 8):
		return None

	f0=1;f1=1;

	for i in range(X.shape[0]):
		if(Y[i]==1):
			f0=0
		else:
			f1=0
	if f0:
		return Node('N')
	if f1:
		return Node('Y')
	Et=total_entropy(X,Y)
	max_i= get_max(X,Y,Et,lookup)
	lookup.append(max_i)
	node = Node(max_i)
	X1=[]
	Y1=[]
	X2=[]
	Y2=[]
	for i in range(X.shape[0]):
		if X[i][max_i] == 0:
			X1.append(X[i])
			Y1.append(Y[i])
		else:
			X2.append(X[i])
			Y2.append(Y[i])
	X1 = np.reshape(np.array(X1),(-1,X.shape[1]))
	X2 = np.reshape(np.array(X2),(-1,X.shape[1]))
	Y1=np.array(Y1)
	Y2=np.array(Y2)
	node.left= train(X1,Y1,lookup)
	node.right= train(X2,Y2,lookup)
	return node

def main():
	X,Y = get_data('data2.csv',1)
	root = train(X,Y,[])
	T = get_data('test2.csv',0)
	out_str = ""
	for i in range(4):
		temp=root
		while(temp):
			if(temp.data == 'N'):
				out_str+="0 "
				break
			elif(temp.data =='Y'):
				out_str+="1 "
				break
			if T[i][temp.data] == 0:
				temp = temp.left
			else:
				temp = temp.right
	print(out_str)
	f = open("16IE10002_2.out",'w')
	f.write(out_str)
	f.close()
main()
	
