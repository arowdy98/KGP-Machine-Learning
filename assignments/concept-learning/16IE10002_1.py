#16IE10002 
#Aditya Rathore 
#Assignment-1 
#python 16IE10002_1.py <input filename>

import sys
import csv
import numpy  as np 

if len(sys.argv) != 2:
	print "The input filename is missing"
	exit()
else :
	file=sys.argv[1]
data=[]
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)
data=np.array(data)
X=data[:,:8]
Y=data[:,8]
#print X
#print Y
H = range(8)
for i in range(8):
	H[i]=0

for i in range(len(Y)):
	if(Y[i]=='1'):
		for j in range(8):
			if H[j]==0:
			    if X[i][j] == '1':
				    H[j]=1
			    else:
					H[j]=-1
			elif (H[j] ==1 and X[i][j] =='0') or (H[j]==-1 and X[i][j]=='1'):     #2 is Dont care
				H[j]=2
count=0
for i in range(8):
    if (H[i] == 1) or (H[i] == -1):
    	count+=1
print count,',',
for i in range(8):
	if (H[i]==1) or (H[i] ==-1):
		print H[i]*(i+1),',',