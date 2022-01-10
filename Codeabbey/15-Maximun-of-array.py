max = 0
min = float('inf')

for x in input().split():
	if int(x) > max:
		max = int(x)
	if int(x) < min:
		min = int(x)
print(str(max)+' '+str(min))