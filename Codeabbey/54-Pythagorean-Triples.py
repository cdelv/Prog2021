import math

def triplet(S):
	for i in range(1,S):
		a = S-i
		N = i*i-a*a
		D = -2*a
		if N%D==0:
			j = N/D
			k=math.sqrt(i*i+j*j)
			return int(k*k)
	return 0

def main():
	answer = []
	for i in range(int(input())):
		S = int(input())
		answer.append(str(triplet(S)))
	print(' '.join(answer))

if __name__ == '__main__':
	main()