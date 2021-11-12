import math

def f(x,A,B,C,D):
	return A*x+B*math.sqrt(x**3)-C*math.exp(-x/50)-D

def binary_search(xl, xu, eps, A, B, C, D, max_iter=100000):
	xr = xl

	for i in range(max_iter):
		
		xr=(xl+xu)/2
		if abs(f(xr,A,B,C,D)) <= eps:
			break
		elif f(xr,A,B,C,D)*f(xl,A,B,C,D) < 0:
			xu = xr
		else:
			xl = xr

	return xr
	
tests = int(input())
tests_case = []
answer = []
eps = 0.0000001
xu = 100
xl = 0

for test in range(tests):
	A, B, C, D = [float(x) for x in input().split()]
	tests_case.append([A,B,C,D])

for i in tests_case:
	root = binary_search(xl,xu,eps,i[0],i[1],i[2],i[3]) 
	answer.append(root)

answer = [str(x) for x in answer]
print(' '.join(answer))

