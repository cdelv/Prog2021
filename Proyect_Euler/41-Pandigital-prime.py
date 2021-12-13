import math

def is_prime(num):
	if num <= 1 or (num % 2 == 0 and num > 2): 
		return False
	return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))


def is_pandigital(num):
	digits = len(str(num))

	if digits>9:
		return False

	aux = []
	n = []
	for j in str(num):
		n.append(j)
	n.sort()

	for i in range(1,digits+1):
		aux.append(str(i))

	if ''.join(aux)==''.join(n):
		return True
	else:
		return False

def main(): 
	num  = 0
	for i in range(1, 7652413):
		if is_pandigital(i):
			if is_prime(i):
				num = i

	print(num)


if __name__ == '__main__':
	main()
