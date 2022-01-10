'''
import math

def is_prime(n):
	if n <= 1 or (n % 2 == 0 and n > 2): 
		return False
	return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def prime_factors(n):
	factors = []
	if is_prime(n) or n==1:
		return [1,n]

	for i in range(2,n):
		if is_prime(i):
			if n%i==0:
				n/=i
				factors.append(i)

	return list(set(factors))

def main():
	for i in range(10000,100000000):
		a=len(prime_factors(i))==4
		if a:
			b=len(prime_factors(i+1))==4
			if b:
				c=len(prime_factors(i+2))==4
				if c:
					d=len(prime_factors(i+3))==4
					if d:
						print(i)
						break


if __name__ == '__main__':
	main()
	#This try was a total fail, was super slow. Trying something faster.
'''
import array, math
import itertools

#fast integer floor sqrt root
def my_sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y

#dynamic programing 
class memoize:
	
	def __init__(self, func):
		self.func = func
		self.cache = {}
	
	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			val = self.func(*args)
			self.cache[args] = val
			return val

@memoize
def count_distinct_prime_factors(n):
	count = 0
	while n > 1:
		count += 1
		for i in range(2, my_sqrt(n) + 1):
			if n % i == 0:
				while True:
					n //= i
					if n % i != 0:
						break
				break
		else:
			break  # n is prime
	return count

def compute():
	cond = lambda i: all((count_distinct_prime_factors(i + j) == 4) for j in range(4))
	ans = next(filter(cond, itertools.count()))
	return str(ans)


if __name__ == "__main__":
	print(compute())