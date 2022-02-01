from math import comb

answer = []
for x in range(int(input())):
    n, k = [int(x) for x in input().split()]
    answer.append(str(comb(n,k)))
print(' '.join(answer))
        
