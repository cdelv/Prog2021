answer = []
N = int(input())
for i in range(N):
    pa, pb = [int(x) for x in input().split()]
    pa /= 100
    pb /= 100
    answer.append(100*(pa / (1 - (1 - pa) * (1 - pb))))

print(' '.join([str(round(x)) for x in answer]))

