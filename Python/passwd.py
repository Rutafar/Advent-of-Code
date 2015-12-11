#! usr/bin/python
import re

def checkZ(passw, i):
	size = len(passw)
	if passw[size-1-i] is 'z':
		b= passw[:size-1-i] + 'a'+ passw[size-i:]
		passw=b
		i+=1
		passw =checkZ(passw, i)
	else:
		b= passw[:size-1-i]+ chr(ord(passw[size-1-i])+1) + passw[size-i:]
		passw=b
	return passw


def newPass(passw):
	if passw is 'abcdefgh':
		return 'abcdffaa'
	elif passw is 'ghijklmn':
		return 'ghjaabcc'
	else:
		passw = checkZ(passw,0)	
	return passw


def straight(passw):
	s=False
	for i in range(len(passw)-3):
		if (passw[i+1]==chr(ord(passw[i])+1)) and (passw[i+2]==chr(ord(passw[i])+2)):
			s=True 
	return s

def confusing(passw):
	f=['i','l','o']
	bad= False
	for c in f:
		if c in passw:
			bad=True
	return bad


def pairs(passw):
	num = re.findall(r"(.)\1", passw)

	if len(num)>=2:
		return True
	else:
		return False

passw='hepxcrrq'
good=False

while not good:
	passw= newPass(passw)
	if(straight(passw) and not confusing(passw) and pairs(passw)):
		good=True

print (passw)
