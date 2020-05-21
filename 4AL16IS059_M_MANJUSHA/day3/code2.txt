#include <stdio.h>
#include <stdlib.h>

//node sructure
typedef struct list 
{
	int data;
	struct list *next;
}node;

int length(node *temp);

int main()
{
	node *head=NULL,*temp,*temp1;
	int choice,count;
	//building linked list
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
		printf("\nIf you wish to add more data on the list enter 1 : ");
		scanf("%d",&choice);
	}while(choice==1);
	
	//Now counting the length of the list using a user defined function
	count=length(head);
	printf("\nThe length of the list is : %d",count);
	
	return 0;
}

//function to find length iteratively
int length(node *temp) 
{
	int c=0;
	//travarsing to the end of the list and count the number of nodes
	while(temp!=NULL)	
	{
		c=c+1;
		temp=temp->next;
	}
	return c;
}
