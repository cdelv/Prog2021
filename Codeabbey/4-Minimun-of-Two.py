a = input()
Sum = []
for i in range(int(a)):
	c, b = input().split()
	if int(c) < int(b):
		Sum.append(str(c))
	else:
		Sum.append(str(b))

print(' '.join(Sum))