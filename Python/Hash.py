#! usr/bin/python
import hashlib
input="iwrupvqb"
i=1
while True:
	md=hashlib.md5()
	toHash = input + str(i)
	print "Trying: " +toHash
	md.update(toHash)
	dig=md.hexdigest()
	if dig[:6]=='000000':
		print toHash
		break
	i+=1
