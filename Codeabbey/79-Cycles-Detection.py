import networkx as nx

G = nx.DiGraph()
ans = []
for _ in range(int(input())):
	nodes = input().split()
	nodes.pop(0)
	G.clear()
	for node in nodes:
		G.add_edge(node[0], node[2])
		G.add_edge(node[2], node[0])
	count=0	
	for cycle in nx.simple_cycles(G):
		if len(cycle)>2:
			count+=1

	if count!=0:
		ans.append(str(1))
	else:
		ans.append(str(0))

print(' '.join(ans))
