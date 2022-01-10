def colatz(x):
	count = 0
	while(x!=1):
		if x%2==0:
			x/=2
		else:
			x=3*x+1
		count+=1
	return count

def main():
	input()
	numbers = [int(x) for x in input().split()]
	answer = []
	for i in numbers:
		answer.append(str(colatz(i)))
	print(' '.join(answer))

if __name__ == '__main__':
	main()