#include<iostream>

int main(void)
{
  long int suma=0;
  for (int ii=1; ii<1000; ii++)
    {
      if (ii%3==0 || ii%5==0)
	{
	  suma += ii;
	}
    }
  std::cout<<suma<<std::endl;
	 
  return 0;
}
