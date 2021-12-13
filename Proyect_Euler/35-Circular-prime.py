import math
from itertools import permutations
from collections import deque


def is_prime(num):
	if num <= 1 or (num % 2 == 0 and num > 2): 
		return False
	return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

def is_circular(num):
	s = str(num)
	return all(is_prime(int(s[i : ] + s[ : i])) for i in range(len(s)))

def compute():
	primes = []
	for x in range(1000000):
		if is_prime(x):
			primes.append(x)

	circular = []
	for prime in primes:
		if is_circular(prime):
			circular.append(prime)

	print(len(circular))
	print(circular)
		
compute()