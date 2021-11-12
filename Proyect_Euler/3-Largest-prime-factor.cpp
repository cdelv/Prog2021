// programa que imprime el mayor factor primo. Carlos Andres del Valle
#include <iostream>
#include <cmath>

int isprime(long int m);
int largest_prime_factor(long int m);

int main(void)
{
  std::cout << largest_prime_factor(600851475143) << std::endl;
  
  return 0;
}

int isprime(long int m)
{
  if (m == 1) return 0;
  int flag = 1;
  for(long int ii = 2; ii <= std::sqrt(m); ++ii) {
    if (m%ii==0) {
      flag = 0;
      break;
    }
  }
  return flag;
}


int largest_prime_factor(long int m)
{
  long int max_factor;
  for (long int k= 2; k <= m; ++k){
    if (m%k == 0 and (isprime(k)== 1)) {
      max_factor =k;
      m/=k;
    }
  }
  return max_factor;
}
