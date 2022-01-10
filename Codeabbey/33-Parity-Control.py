message = [int(x) for x in input().split()]
bin_message = [list(bin(x)[2:].zfill(8)) for x in message]
answare = []

Sum=0
for i in bin_message:

	for j in i:
		Sum+=int(j)

	if Sum%2==0:
		answare.append(i)

	Sum=0

for i in answare:
	if int(i[0])==1:
		i[0]="0"

answare = [''.join(ele) for ele in answare]
answare = [chr(int(x, 2)) for x in answare]

print(''.join(answare))