try:
	x1 = set(input().split(','))
	x2 = set(input().split(','))
	x3 = list(x1.union(x2)-x1.intersection(x2))
	l=str('')
	for i in x3:
	    l=i+' '+l
	l=l[:-1]
	print(l)
except:
	print('just Error')
	print('blllyaaaaa')