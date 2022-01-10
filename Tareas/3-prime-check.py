import time
from math import sqrt

def is_prime_good(num):
  if num <= 1 or (num % 2 == 0 and num > 2): 
    return False
  return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))

def is_prime_bad(n):
    if (n<=1):
        return False
    #elif (n==2):
    #    return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True 




start = time.time()
print(is_prime_bad(2))
end = time.time()

print(end - start)


start = time.time()
print(is_prime_good(10000000))
end = time.time()

print(end - start)