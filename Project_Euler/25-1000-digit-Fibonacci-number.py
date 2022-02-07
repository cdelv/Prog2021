from functools import cache, lru_cache

@lru_cache(maxsize=25)
def Fibonacci(n):
	if n <= 1:
		return n
	return Fibonacci(n-1) + Fibonacci(n-2)

def main():
	digits = 0
	i = 1
	while digits < 1000:
		digits = len(str(Fibonacci(i)))
		i+=1

	print(i-1)

if __name__ == '__main__':
	main()
		