def compute():
	# hacer la suma de los divisores
	divisorsum = [0] * 10000
	for i in range(1, len(divisorsum)):
		for j in range(i * 2, len(divisorsum), i):
			divisorsum[j] += i
	
	# encontrar todas las parejas amicables
	ans = 0
	for i in range(1, len(divisorsum)):
		j = divisorsum[i]
		if j != i and j < len(divisorsum) and divisorsum[j] == i:
			ans += i
	return str(ans)


if __name__ == "__main__":
	print(compute())