T=raw_input()
T=int(T)
while T:
	n=raw_input()
	m,n=n.split()
	m=int(m)
	n=int(n)
	s=0
	while m:
		s=s+n/m
		m,n=n%m,m
	print s
	T=T-1
