f = input()
Sum = []

for i in range(int(f)):
	summ=0
	a, b, c = input().split()
	num = int(a)*int(b)+int(c)
	for j in str(num):
		summ+=int(j)

	Sum.append(str(summ))
    
print(' '.join(Sum))