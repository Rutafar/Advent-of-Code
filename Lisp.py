#! usr/bin/python

f=open('floors.txt', 'r')
floor=0
position=0
first = False
for line in f:
	for ch in line:
		position += 1
		if ch is '(':
			floor +=1
		elif ch is ')':
			floor-=1
		if floor ==-1 and not first:
			first = True
			print "Santa reached -1 floor on: " + str(position)
print "Santa is on floor: " + str(floor)
