#! usr/bin/python


def countLights(lights):
	nl=0
	for i in range(1000):
		for j in range(1000):
			if lights[i][j]==1:
				nl+=1
	print nl
def main():
	lights=[[0 for i in range(1000)] for j in range(1000)]
	f=open('lights.txt','r')
	for line in f:
		if 'turn on' in line:
			line=line.split('through')
			line_x= line[0][8:]
			start = [i for i in map(int, line_x.split(','))]
			end = [i for i in map(int, line[1].split(','))]
			for x in range(start[0], end[0]+1):
				for y in range(start[1],end[1]+1):
					lights[x][y]=1
		elif 'turn off' in line:
			line=line.split('through')
			line_x= line[0][9:]
			start = [i for i in map(int, line_x.split(','))]
			end = [i for i in map(int, line[1].split(','))]
			for x in range(start[0], end[0]+1):
				for y in range(start[1],end[1]+1):
					lights[x][y]=0
		elif 'toggle' in line:
			line=line.split('through')
			line_x= line[0][7:]
			start = [i for i in map(int, line_x.split(','))]
			end = [i for i in map(int, line[1].split(','))]
			for x in range(start[0], end[0]+1):
				for y in range(start[1],end[1]+1):
					if lights[x][y]==0:
						lights[x][y]=1
					elif lights[x][y]==1:
						lights[x][y]=0
	
	countLights(lights)

if __name__=='__main__':
	main()
