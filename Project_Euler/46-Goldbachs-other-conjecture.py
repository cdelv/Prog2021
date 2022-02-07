import math

def is_prime(n):
	if n <= 1 or (n % 2 == 0 and n > 2): 
		return False
	return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def Golbach(n):
	#the conjecture says that n = prime + 2*m^2
	#then n - 2*m^2 must be prime, then we must seak for a combination that is not prime
	#there are not negative primes
	for m in range(int(math.sqrt(n/2))+2):
		a = n-2*m**2
		if is_prime(a):
			return True

	return False

def main():
	for i in range(9,1000000,2):
		if not is_prime(i):
			if not Golbach(i):
				print(i)
				break

if __name__ == '__main__':
	main()