import math as m  

def calculate_pi(K, N):
	R = int(10**K)
	Side = R
	for i in range(N):
		d = Side//2
		h = m.isqrt(R*R - d*d)
		Side = m.isqrt(d*d + (R-h)*(R-h))

	return 6*(2**N)*Side//2


K, N = map(int, input().split())

print(calculate_pi(K, N))