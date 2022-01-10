lenght, types = input().split()
numbers = input().split()
answer = []

for i in range(1,int(types)+1):
	answer.append(str(numbers.count(str(i))))

print(' '.join(answer))


