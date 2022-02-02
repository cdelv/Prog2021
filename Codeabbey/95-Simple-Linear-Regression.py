import numpy as np
import scipy.stats as ss

S, F = [int(x) for x in input().split()]
x = []
y = []
for i in range(F-S+1):
	point = input().split()
	point.pop(0)
	x.append(float(point[0]))
	y.append(float(point[1]))


slope, intercept, r, p, se = ss.linregress(np.asarray(x), np.asarray(y))
print(slope, end=' ')
print(intercept)
