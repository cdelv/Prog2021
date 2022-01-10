import math


def function(a,b):
	return a**b

def clean(l):
	x = []
	for a in l:
	    if a not in x:
	      x.append(a)
	return x

def main():
	ans = []
	for a in range(2,101):
		for b in range(2,101):
			ans.append(function(a,b))

	print(len(clean(ans)))
			

if __name__ == '__main__':
	main()