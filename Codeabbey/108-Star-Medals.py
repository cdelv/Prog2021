def count_gems(N, T):
	if T == 1:
		return 0

	
	return N*(T-1)


Answer = []

for _ in range(int(input())):
    N, T = map(int, input().split())
    Answer.append(count_gems(N, T))
    

print(' '.join(map(str, Answer)))