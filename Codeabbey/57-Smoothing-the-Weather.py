def main():
	input()
	data = [float(x) for x in input().split()]
	answare = []
	answare.append(data[0])
	for i in range(1,len(data)-1):
		answare.append((data[i-1]+data[i]+data[i+1])/3)

	answare.append(data[len(data)-1])
	answare = [str(x) for x in answare]
	print(' '.join(answare))


if __name__ == '__main__':
	main()