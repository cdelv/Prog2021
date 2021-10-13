a = input()
answer = []
array = []
for i in range(int(a)):
	array = [int(x) for x in input().split()]
	del array[-1]
	answer.append(str(round(sum(array) / len(array))))

print(' '.join(answer))
