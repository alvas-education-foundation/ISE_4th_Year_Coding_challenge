#include <stdio.h>
#include <stdlib.h>

typedef struct list  //linked list node
{
	int data;
	struct list *next;
}node;

int main()
{
	node *head=NULL,*temp,*temp1;
	int choice,count=0,key;

	//building the linked list
	do
	{
		temp=(node *)malloc(sizeof(node));
		if(temp!=NULL)
		{
			printf("\nEnter the element in the list : ");
			scanf("%d",&temp->data);
			temp->next=NULL;
			if(head==NULL)
			{	
				head=temp;
			}
			else
			{
				temp1=head;
				while(temp1->next!=NULL)
				{
					temp1=temp1->next;
				}
				temp1->next=temp;
			}
		}
		else
		{
			printf("\nMemory not avilable...node allocation is not possible");
		}
		printf("\nIf you wish to add m ore data on the list enter 1 : ");
		scanf("%d",&choice);
	}while(choice==1);
	
	//finding occurence of key
	printf("\nEnter the data to find it's occurrence : ");
	scanf("%d",&key);
	
	temp=head;
	while(temp!=NULL)
	{
		if(temp->data==key)
		{
			count=count+1;
		}
		temp=temp->next;
	}
	printf("\n %d occurred %d times in the list",key,count);

	return 0;
}
