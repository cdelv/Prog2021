import math

def std(data):
	mu = sum(data)/len(data)
	Sum = 0
	for i in data:
		Sum+=(i-mu)**2

	return math.sqrt(Sum/len(data))

def main():
	n = input()
	Ans = []
	for i in range(int(n)):
		Stock = input().split()
		data = Stock[1:]
		data = [int(x) for x in data]
		s = std(data)
		print(s)
		if s >= 4*0.01*sum(data)/len(data):
			Ans.append(Stock[0])

	print(' '.join(Ans))

if __name__ == '__main__':
	main()