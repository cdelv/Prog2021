import math
def findIndex(n) :
	if n==0:
		return 0

	fibo = 2.078087 * math.log(n) + 1.672276 #usando la fórmula
	return round(fibo)

def main():
	ans = []
	for i in range(int(input())):
		ans.append(findIndex(int(input())))

	ans = [str(x) for x in ans]
	print(' '.join(ans))

if __name__ == '__main__':
	main()