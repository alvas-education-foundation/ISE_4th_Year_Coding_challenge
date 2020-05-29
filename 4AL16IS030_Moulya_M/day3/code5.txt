#include <stdio.h>

int main()
{
	unsigned int n;
	printf("enter the integer\n");
	scanf("%d",&n);
	int count=0,store=-1;
	while(n!=0){
		if(n & 1 == 1) //if current bit is set
			store=count; //update store
		n=n>>1; //right shift
		count++; //increase count
	}

	if(store==-1){//if store not updated
		printf("No bit is set\n"); //no set bit present at all
		return 0;
	}
	printf("Highest bit set ");
	//printing highest set bit
	printf("in its binary representation: %d \n",store); 

	return 0;
}
