T=raw_input()
T=int(T)
while T:
	n=raw_input()
	a=n.split()
	
	n=int(a[0])
	b=[0]*10
	j=0
	count=0
	for x in range (-101,101):
		s=0
		for i in range (1,n+2):
			s=s+int(a[i])*(x**(i-1))
		if s==0:
			b[j]=x
			j=j+1
			
	for i in range(0,j):
		print b[i],
	if j==0:
		print "NO"
	else:
		print
	T=T-1			
	
