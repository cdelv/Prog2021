a = input()
Sum = []
for i in range(int(a)):
	b, c, d = input().split()
	Sum.append(str(min(int(b),int(c),int(d))))

print(' '.join(Sum))