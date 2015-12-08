#! usr/bin/python
import re
ops={}
result={}
def main():
	f = open ('ops.txt','r')
	for line in f:
		line = line.split('->')
		ops[line[1].strip()]=line[0].strip().split(' ')
	value=calc('a')
	print value


def calc(wire):
	try:
		return int(wire)
	except ValueError:
		pass

	if wire not in result:
		toDo = ops[wire]
		if len(toDo)==1:
			res = calc(toDo[0])
		elif 'AND' in toDo:
			res = calc(toDo[0]) & calc(toDo[2])
		elif 'OR' in toDo:
			res = calc(toDo[0]) | calc(toDo[2])
		elif 'RSHIFT' in toDo:
			res = calc(toDo[0])>> calc(toDo[2]) 
		elif 'LSHIFT' in toDo:
			res = calc(toDo[0])<< calc(toDo[2])
		elif 'NOT' in toDo:	
			res = ~calc(toDo[1])
	
		result[wire]=res
	return result[wire]


if __name__ == '__main__':
	main()
