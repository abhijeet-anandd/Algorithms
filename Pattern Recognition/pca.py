import numpy as np
f=int(input("Enter the number of features : "))
features=[]
for F in range(f):
	temp=list(map(float,input("Enter values of feature %d : "%(F+1)).split()))
	features.append(temp)
features=np.array(features)

k=int(input("Enter the number of dimensions needed finally : "))
covar=np.cov(features)
print("Σ = ")
print(covar)
eigen_values,eigen_vectors=np.linalg.eig(covar)
print("Eigen Values found : ")
print(eigen_values)
print("Eigen vectors found : ")
print(eigen_vectors)
eigen_sorted=np.argsort(np.absolute(eigen_values))[f-k:]
print(eigen_sorted)
print("Final adjust Principal Component V = ")
print(eigen_vectors[eigen_sorted][:,eigen_sorted])

