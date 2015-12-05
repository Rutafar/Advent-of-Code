#! usr/bin/python
import re
def numOfVowels(word):
	nVowels=0
	for v in vowels:
		nVowels+=word.count(v)
	return nVowels

def Twice(word):
	num = re.findall(r"(.)\1", word)
	if len(num)>=1:
		return True
	else:
		return False 

forbidden=['ab','cd','pq','xy']
vowels=['a','e','i','o','u']
f=open('words.txt','r')
goodString=0
for word in f:
	
	if any(x in word for x in forbidden):
		continue
	nv=numOfVowels(word)
	if nv>=3 and Twice(word):
		goodString+=1
print str(goodString)
