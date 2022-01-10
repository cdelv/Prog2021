import math
import numpy as np

def is_prime(num):
  if num <= 1 or (num % 2 == 0 and num > 2): 
    return False
  return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

def q_formula(x,a,b):
	return x*x+a*x+b


def main():
	tries = []
	n=0
	for a in range(-1000,1000):
		for b in range(-1001,1001):
			while (is_prime(q_formula(n,a,b))):
				n+=1
			tries.append([a,b,n])
			n=0

	A, B, T = 0, 0, 0
	for i in tries:
		if i[2] > T:
			T = i[2]
			A = i[0]
			B = i[1]

	print(A*B)

if __name__ == '__main__':
	main()