f = input()
answer = []
numbers = input().split()

for i in numbers:
	Sum = 0
	iterator = 1

	for digit in i:
		Sum+=int(digit)*iterator
		iterator+=1

	answer.append(str(Sum))

print(' '.join(answer))
