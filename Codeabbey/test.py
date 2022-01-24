def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def calc_fib(n,m):
    p = pisanoPeriod(m)
    n = n % p
    if (n <= 1):
        return n
    else:
      previous,current = 0,1
      for i in range(2,n+1):
        previous,current = current,(previous+current)
    return current%m

n,m =map(int,input().split(" "))
print(calc_fib(n,m))