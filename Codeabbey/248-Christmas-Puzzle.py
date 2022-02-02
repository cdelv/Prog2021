specs = [int(x) for x in input().split()]
sections = len(specs)//3
tree = []
for i in range(sections):
	for j in range(specs[3*i]):
		lines = specs[3*i+1]+2*j*specs[3*i+2]
		tree.append('+'*lines)
lines =0
for k in tree:
	if len(k)>lines:
		lines = len(k)
for k in tree:
	print(' '*((lines-len(k))//2),k)