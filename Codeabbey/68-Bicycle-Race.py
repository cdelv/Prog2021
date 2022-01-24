def distance(s,a,b):
	#create the system of eq and solve it
	# x=a*t     primer ciclista
	# x=s-b*t   segundo ciclista
	# x=s-b*(x/a) --> x*(1+b/a)=s
	return s/(1+b/a)

def main():
	ans = []
	for i in range(int(input())):
		s, a, b = [float(x) for x in input().split()]
		ans.append(str(distance(s,a,b)))

	print(' '.join(ans))

if __name__ == '__main__':
	main()