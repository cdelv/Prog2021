#include <iostream>

int main()
{	
	int n = 20;
	long long int routes = 1;
	int i = 1;

	while(i <= n)
	{
		routes = routes * (2 * n - i + 1) / i;
		++i;
	}

	std::cout << routes << std::endl;

	return 0;
}
