#! usr/bin/python
def howFar(vel, t1, rest):
	vel = int(vel)
	t1= int(t1)
	rest= int(rest)
	time = 0
	distance=0
	while time+t1<2503:
		distance += vel*t1
		time += t1 + rest
	return distance


f = open('reindeer.txt', 'r')
dict ={}
for line in f:
	line=line.split()
	dis=howFar(line[3], line[6], line[13]) 
	dict[line[0]]=dis

print dict
