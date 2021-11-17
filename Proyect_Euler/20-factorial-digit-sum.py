import math

n = math.factorial(100)
ans = sum(int(c) for c in str(n))
print(str(ans))