a = input()
Sum = []
for i in range(int(a)):
	c, b = input().split()
	Sum.append(str(int(c)+int(b)))

print(' '.join(Sum))

