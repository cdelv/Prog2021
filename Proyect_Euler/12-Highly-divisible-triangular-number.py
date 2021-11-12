from math import sqrt

def factors(n):
   number_of_factors = 1

   for i in range(2, int(sqrt(n)) + 1):
      if n % i == 0:
         number_of_factors += 2

   return number_of_factors

n, tri_num = 1, 1

while factors(tri_num) <= 500:
   n += 1
   tri_num = int(n * (n + 1) / 2)

print(tri_num)