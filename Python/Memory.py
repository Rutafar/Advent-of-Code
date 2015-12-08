#! usr/bin/python
import re
f=open('strings.txt', 'r')
P1=0
P2=0
for line in f:
	line= line.strip()
	print (len(line) ,len(eval(line)))
	P1 += len(line) - len(eval(line))
	P2 += len(re.escape(line))+2-len(line)
	
print (P1, P2)
