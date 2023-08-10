import math as m
answer = []
for i in range(int(input())):
    D1, A, B = [float(x) for x in input().split()]
    A *= m.pi/180
    B *= m.pi/180
    H = m.tan(A)*D1/(1 - m.tan(A)/m.tan(B))
    answer.append(H)

print(' '.join([str(round(x)) for x in answer]))