import math

N = int(input())
H = []

for i in range(N):
    D, B = [float(x) for x in input().split()]
    A = B - 90.0
    H.append(D*math.tan(A*math.pi/180))

print(' '.join([str(round(x)) for x in H]))