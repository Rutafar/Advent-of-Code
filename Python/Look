#! usr/bin/python
from itertools import groupby
input='1321131112'

for i in range(50):
	tmp=''
	for a in [[k,len(list(g))] for k, g in groupby(input)]:
		tmp+=str(a[1])+ a[0]
	input = tmp
print len(input)
