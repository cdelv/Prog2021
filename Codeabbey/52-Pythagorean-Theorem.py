def clasify(data):
	left =  data[0]**2+data[1]**2
	right = data[2]**2
	if left==right:
		return 'R'
	elif left<right:
		return 'O'
	elif left>right:
		return 'A'
	else:
		return 'ERROR'

def main():
	answer = []
	for i in range(int(input())):
		data = [int(x) for x in input().split()]
		answer.append(clasify(data))

	print(' '.join(answer))



if __name__ == '__main__':
	main()