s=int(raw_input("Enter the number of samples in training data : "))
c=int(raw_input("Enter the number of classes : "))
text=[]
for S in xrange(s):
	temp=raw_input("Enter sample text %d : "%S).lower()
	temp=temp.replace('.', ' ').strip().split()
	text.append(temp)
cl=raw_input("Enter the classes of each text separated by space respectively : ").strip().split()
cl_set=list(set(cl))
words={}
for S in xrange(s):
	for w in set(text[S]):
		ct=text[S].count(w)
		print w
		if w not in words.keys():
			temp=[0]*c
			words[w]=temp
		words[w][cl_set.index(cl[S])]=words[w][cl_set.index(cl[S])]+ct
print words
unk=raw_input("Enter Text to be classified : ").lower().replace('.',' ').strip().split()

unk_set=set(unk)
apri=[]
for n in xrange(len(cl_set)):
	apri.append(float(cl.count(cl_set[n]))/float(len(cl)))
ct_class=[]
for C in xrange(c):
	temp=0
	for w in words.keys():
		temp=temp+words[w][C]
	ct_class.append(temp)

cl_con=[]
for C in xrange(c):
	temp=1
	for w in unk_set:
		nk=words[w][C]
		p=float(nk+1)/float(ct_class[C]+len(words.keys()))
		temp=temp*p
	cl_con.append(temp)

px=1
n=0
for w in words.keys():
	n=n+sum(words[w])
for w in unk_set:
	px=px*(float(sum(words[w]))/float(n))

post=[]
for n in xrange(len(cl_set)):
	post.append(cl_con[n]*apri[n]/px)

l=post.index(max(post))

print "The prediction is : " + cl_set[l]
print "The probability of correctness is : "+str(post[l])