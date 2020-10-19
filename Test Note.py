def f(a, L=[]):
	    L.append(a)
	    return L
def f1(x,y=3,z=9):
    print(str(x) +", "+str(y)+", "+str(z))
print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(5, ["Hello1"]))
print(f1(x=12,z=19))

L = ['E','F','B','A','D','I','I','C','B','A','D','D']
d = {}
for m in L:
	if m in d:
		d[m] = d[m] + 1
	else:
		d[m] = 1
print (d)


def last_four(x):
	return x[ -4:]


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
print(last_four(ids[0]))