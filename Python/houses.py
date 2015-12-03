#! usr/bin/python

coord=set()
satan_x=0
satan_y=0
robot_x=0
robot_y=0
coord.add((satan_x,satan_y))
isSatan=True
f=open('houses.txt', 'r')
for line in f:
	for ch in line:
		if isSatan:
			if ch is '^':
				satan_y+=1
			if ch is 'v':
				satan_y-=1
			if ch is '<':
				satan_x-=1
			if ch is '>':
				satan_x+=1
			coord.add((satan_x,satan_y))
			isSatan=False
		else:
			if ch is '^':
				robot_y+=1
			if ch is 'v':
				robot_y-=1
			if ch is '<':
				robot_x-=1
			if ch is '>':
				robot_x+=1
			coord.add((robot_x,robot_y))
			isSatan=True
print len(coord)
