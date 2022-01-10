//calcula la suma de los terminos pare menor a 4M de la serie de
//Fibonachi
#include<iostream>

int main (void)
{
  int suma=2; //la suma empieza en 2 porque el termino 2 de la serie es par
  int a0=1;
  int a1=2;
  int an=0; //an empieza en el termino 3
  
   while (an<=4000000)
    {
      an=a1+a0;
      //std::cout<<an<<"\n";
      if (an%2==0)
	{
	  suma+=an;
	}
      a0=a1;
      a1=an;
    }
  std::cout<<suma << "\n";
  
  return 0;
}
