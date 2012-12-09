import sys
T=int(raw_input())
while T:
	n=raw_input()
	m,n=n.split()
	m=int(m)
	l=len(n)
	m=m%l
	j=0
	for i in range(m,l):
		sys.stdout.write(n[i])
	for i in range(0,m):
		sys.stdout.write(n[i])
	print
	T=T-1
