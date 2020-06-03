#include<stdio.h>

void loopingFunc(int d)
{
	if(d==15)
	{
		for(int i=0; i<3; i++)
		{
			printf("Subscribe\n");
		}
	}
}

int main()
{
	int a, b, c;
	
	a = 5;
	b = 10;
	c = a + b;

	loopingFunc(c);
	
	return 0;
}
