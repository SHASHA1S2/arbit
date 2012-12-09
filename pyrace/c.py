def rec(x,y):
	if x==0:
		return y+1
	if x>0 and y==0:
		return rec(x-1,1)
	if x>0 and y>0:
		return rec(x-1,rec(x,y-1))
	

T=raw_input()
T=int(T)

while T:
	n=raw_input()
	m,n=n.split()
	m=int(m)
	n=int(n)
	if m>=0 and n>=0:
		print rec(m,n)
	T=T-1
	
