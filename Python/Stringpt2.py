#! usr/bin/python
import re
def main():
	niceString=0
	f=open('words.txt','r')
	for word in f:
		gap=re.findall(r'(.).\1',word)
		num= re.findall(r'(.)(.)(.*?)\1\2', word)
		if len(num)>=1 and len(gap)>=1:
			niceString+=1
	print niceString	
	


if __name__ == '__main__':
	main()
