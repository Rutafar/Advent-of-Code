#! usr/bin/python

f=open('dimensions.txt', 'r')
ribbon=0
wrapping=0
for line in f:
	for l in line.split("\n "):
		l,w,h=map(int, l.split("x"))
		wrapping += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
		ribbon += (2*l*w*h - 2* max(l,w,h)) + l*w*h
print "Wrapping needed: " + str(wrapping) + " Ribbon needed: " +  str(ribbon)
