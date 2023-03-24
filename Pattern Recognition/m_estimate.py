s=int(raw_input("Enter the number of training data sets : "))
f=int(raw_input("Enter the number of features : "))
c=int(raw_input("Enter the number of classes : "))
feat_vect=[]
for F in xrange(f):
	temp=raw_input("Enter values of feature %d using characters : "%(F+1)).split(' ')
	feat_vect.append(temp)

cl=raw_input("Enter the respective classes using characters : ").split(' ')

pi=map(float,raw_input("Emter the pi (prior expectation) values of each class : "))
m=int(raw_input("Enter the m value : "))

unk=raw_input("Enter the data who's class has to be predicted : ").split(' ')

cl_set=list(set(cl))
apri=[]
for n in xrange(len(cl_set)):
	apri.append(float(cl.count(cl_set[n])+m*pi[n])/float(len(cl))+m)


# print apri

cl_con=[]
for n in xrange(len(cl_set)):
	temp=1
	for F in xrange(f):
		temp2=0
		for S in xrange(s):
			if feat_vect[F][S]==unk[F] and cl[S]==cl_set[n]:
				temp2=temp2+1
		temp3=float(temp2+m*pi[n])/float(cl.count(cl_set[n])+m)
		# print temp3
		temp=temp*temp3
	cl_con.append(temp)
# print cl_con

px=1
for F in xrange(f):
	ct=feat_vect[F].count(unk[F])
	print ct
	px=px*(float(ct)/float(s))		
# print px
post=[]
for n in xrange(len(cl_set)):
	post.append(cl_con[n]*apri[n]/px)

l=post.index(max(post))

print "The prediction is : " + cl_set[l]
print "The probability of correctness is : "+str(post[l])