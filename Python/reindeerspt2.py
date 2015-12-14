#! usr/bin/python
f = open('reindeer.txt', 'r')
dict ={}
points={}
dist={}
for line in f:
	line=line.split()
	dict[line[0]]=(int(line[3]), int(line[6]), int(line[13]))
	points[line[0]]=0
	dist[line[0]]=0
for i in range(1, 2504):
	for d in dict:
		dist[d]= dict[d][0]*dict[d][1]*(i/(dict[d][1]+dict[d][2])) + dict[d][0] * min(dict[d][1], i %(dict[d][1] + dict[d][2]))
	for p in points:
		maxi = dist[max(dist, key=dist.get)]
		if dist[p]>= maxi:
			points[p]+=1

print points
