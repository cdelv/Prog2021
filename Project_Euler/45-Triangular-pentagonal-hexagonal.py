from decimal import Decimal as D

def is_triangular(x):
	n = D(0.5)*(D(8)*D(x) + D(1)).sqrt() - D(0.5)
	#print(n)
	return abs(round(n)-n)<=0.000000001

def is_pentagonal(x):
	n = ((D(24)*D(x) + D(1)).sqrt() + D(1))/D(6)
	#print(n,round(n), round(n)-n)
	return abs(round(n)-n)<=0.000000001

def is_hexagonal(x):
	n = D(0.25)*(D(8)*D(x) + D(1)).sqrt() + D(0.25)
	#print(n)
	return abs(round(n)-n)<=0.000000001

def hexagonal(n):
	return n*(2*n-1)

def main():
	#Every hexagonal number is triangular. Then, we have to try only hexagonal numbers.
	#We only have to check if is pentagonal.
	# 40755 is the 143 hexagonal number, so we start at the next one.
	for i in range(144,1000000):
		if is_pentagonal(hexagonal(i)):
			print(i, hexagonal(i))
			break

if __name__ == '__main__':
	main()