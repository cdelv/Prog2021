//calcula el mayor producto palindromo de dos numeros con
//tres cifras
#include<iostream>
#include<vector>
#include <algorithm>

//--------------declaracion de funciones-----------------

bool palindrome_checker(int x); //funcion que revisa si un numero es palindromo
std::vector <int> integerToArray(int x); //convertir numero a vector de digitos


//-------------funcion main------------------------------
int main (void)
{
  std::vector <int> array;
  
  for(int i=100; i<1000; i++)
    for(int j=100; j<1000; j++)
      {
	if(palindrome_checker(i*j))
	  {
	    array.push_back(i*j);
	  }
      }

  std::cout<<*max_element(std::begin(array), std::end(array)) << '\n';
   
  return 0;
}

bool palindrome_checker(int x)
{
  std::vector <int> number=integerToArray(x);

  for(int i=0; i<number.size();i++)
    {
      if (number[0+i]!=number[number.size()-1-i])
	return false;
    }
  return  true;

}
std::vector <int> integerToArray(int x)
{
  std::vector <int> resultArray;
    while (true)
    {
    resultArray.insert(resultArray.begin(), x%10);
    x /= 10;
    if(x == 0)
        return resultArray;
    }
}
