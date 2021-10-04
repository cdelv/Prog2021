f = input()
Sum = []

for i in range(int(f)):
	summ=0
	a, b, c = input().split()
	for j in range(1,int(c)+1):
		summ+=(int(a)+(j-1)*int(b))

	Sum.append(str(summ))
    
print(' '.join(Sum))