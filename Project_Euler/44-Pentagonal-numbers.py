import math

def pentagonal(n):
	return int(n*(3*n-1)/2)

def find_diff(numbers):
	num = 1000000000000
	for i in numbers:
		for j in numbers:
			D = abs(j-i)
			S = j+i
			if D in numbers:
				if S in numbers:
					if num > D:
						num = D
	return num

def main(): #  5482660
	start = 1
	end = 100000
	numbers = []
	for i in range(start,end):
		numbers.append(pentagonal(i))

	print(find_diff(numbers))


if __name__ == '__main__':
	main()