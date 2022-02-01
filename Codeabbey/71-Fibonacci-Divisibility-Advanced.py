from functools import lru_cache
from math import lcm
from functools import reduce

@lru_cache(maxsize=1000)
def fibonacci_modulo(n, m):
    if n <= 1:
        return n % m
    elif n % 2:
        a = fibonacci_modulo(n // 2, m)
        b = fibonacci_modulo(n // 2 + 1, m)
        return (a * a + b * b) % m
    else:
        a = fibonacci_modulo(n // 2 - 1, m)
        b = fibonacci_modulo(n // 2, m)
        return (2 * a + b) * b % m


def prime_factors(n):
    divisors = [ d for d in range(2,n//2+1) if n % d == 0 ]
    #return [ d for d in divisors if \
    #         all( d % od != 0 for od in divisors if od != d ) ]
    return divisors

def div_test(m):
	factors = prime_factors(m)
	P = []
	if len(factors)==0: factors.append(m)
	for i in factors:
		for j in range(1,100*m):
			if fibonacci_modulo(j,i)==0:
				P.append(j)
				break

	r = reduce(lcm, P)
	return r

def main():
	input()
	data = [int(x) for x in input().split()]
	ans = []
	for i in data:
		ans.append(str(div_test(i)))
	print(' '.join(ans))
		

if __name__ == '__main__':
	main()

	