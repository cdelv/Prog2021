def harvest(data, index=0):
	if index>=len(data):
		return 0
	return  data[index]+max([harvest(data,index+2),harvest(data,index+3)])

def main():
	ans=[]
	for _ in range(int(input())):
		data = [int(x) for x in input().split()]
		ans.append(str(harvest(data)))

	print(' '.join(ans))

if __name__ == '__main__':
	main()