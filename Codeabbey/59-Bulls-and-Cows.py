def main():
	code, N = input().split()
	data = input().split()
	ans = []

	for i in data:
		c=0
		nc=0
		correct = []
		for j in range(len(i)):
			if code[j]==i[j]:
				c+=1
				correct.append(j)
		for j in range(len(i)):
			if j not in correct:
				if i[j] in code:
					nc+=1

		ans.append(str(c)+'-'+str(nc))
	print(' '.join(ans))

if __name__ == '__main__':
	main()