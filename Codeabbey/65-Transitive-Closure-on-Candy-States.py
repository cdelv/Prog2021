import networkx as nx

G = nx.Graph()
ans = []
for _ in range(int(input())):
	nodes = input().split()
	G.add_edge(nodes[0], nodes[2])
for _ in range(int(input())):
	nodes = input().split()
	if nx.has_path(G, nodes[0], nodes[2]):
		ans.append(str(nx.shortest_path_length(G, nodes[0], nodes[2])))
	else:
		ans.append(str(10000000))
print(' '.join(ans))