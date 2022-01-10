#include <iostream>
#include <cmath>

int isprime(int m); // returns 1 if a number is prime
void print_primes(int m, int n);

int main(void)
{
  print_primes(0, 10001);
  return 0;
}

int isprime(int m)
{
  if (m == 1) return 0;
  int flag = 1;
  for(int ii = 2; ii <= std::sqrt(m); ++ii) {
    if (m%ii==0) {
      flag = 0;
      break;
    }
  }
  return flag;
}

void print_primes(int m, int n)
{
  int i=0;
  int prime=0;
  for(int ii = m; ii <= n; i++) {
    if (isprime(i)) {
      ii++;
      prime=i;
    }
  }
  std::cout << prime << std::endl;
}
