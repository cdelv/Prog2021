#include<iostream>
#include<cmath>

int main(void)
{
  
  int suma1=0;
  int suma2=0;
  int total=0;

  for(int i=0; i<=100; i++)
    {
      suma1+=std::pow(i,2); 
    }
  for(int j=0; j<=100; j++)
    {
      suma2+=j;
    }
  
  total=std::pow(suma2,2)-suma1;
  
  std::cout<<total <<std::endl;
  return 0;
}
