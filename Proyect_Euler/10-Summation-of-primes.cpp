#include <iostream>
#include <vector>
#include <map>

int main()
{
  long int Max = 2000000;
  std::vector<long int> primes;
  primes.push_back(2);
  
  // revisar todos los numeros impares
  for (long int i = 3; i <= Max; i += 2)
  {
    bool isPrime = true;
    for (auto p : primes)
    {
      if (p*p > i)
        break;
      if (i % p == 0)
      {
        isPrime = false;
        break;
      }
    }
    if (isPrime)
      primes.push_back(i);
  }

  long long int sum = 0;
  for (auto p : primes)
  {
    sum += p;
  }
  std::cout << sum << std::endl;
  
  return 0;
}
