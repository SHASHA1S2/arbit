T=raw_input()
T=int(T)
c=[0]*6
d=[0]*6
c[1]=3
d[1]=4
c[2]=1
d[2]=5
c[3]=2
d[3]=4
c[4]=2
d[4]=5
c[5]=1
d[5]=3
while T:
	n=raw_input()
	m,n=n.split()
	if m[0]=='R':
		a=1
	if m[0]=='P':
		a=2
	if m[0]=='S' and m[1]=='C':
		a=3
	elif m[0]=='S' and m[1]=='P':
		a=5
	elif m[0]=='L':
		a=4
	if n[0]=='R':
		b=1
	if n[0]=='P':
		b=2
	if n[0]=='S' and n[1]=='C':
		b=3
	elif n[0]=='S' and n[1]=='P':
		b=5
	elif n[0]=='L':
		b=4
	if c[a]==b or d[a]==b:
		print m
	elif a==b:
		print "DRAW"
	else:
		print n
	T=T-1
