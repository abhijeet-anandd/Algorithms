import numpy as np
s=int(input("Enter number of training data samples : "))
c=int(input("Enter the numebr of classes : "))
k=int(input("Enter the value of k : "))
data=[]
for S in range(s):
	temp=list(map(float,input("Enter the training data set in the form of x y value : ").split()))
	data.append(temp)
dataset=np.array(data)
x,y=list(map(float,input("Enter the data to be predicted in the form of x y : ").split()))
dist=np.sqrt(np.square(dataset[:,0]-x)+np.square(dataset[:,1]-y))
knn=np.argsort(dist)[:k]
unique, counts = np.unique(dataset[knn,2], return_counts=True)
print(knn)
print(dist)
pred_index=np.argmax(counts)
print("The prediction is : %d"%unique[pred_index])
accuracy=float(counts[pred_index])*100/k
print("The accuracy of prediction is " +str(accuracy)+"%")