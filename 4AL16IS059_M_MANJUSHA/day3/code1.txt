#include <stdio.h>
#include <stdlib.h>

typedef struct list
{
	int data;
	struct list *next;
}node;

void display(node *temp)
{
	node *temp1=temp;
	printf("\nNow the list is :\n%d->",temp->data);
	temp=temp->next;
	while(temp!=temp1)	
	{
		printf("%d->",temp->data);
		temp=temp->next;
	}
	printf("%d\n",temp1->data);
}

int main(){
	node *head=NULL,*temp,*temp1,*temp2;
	int choice,key;
	
	do
	{
		temp=(node *)malloc(sizeof(node));
		if(temp!=NULL)
		{
			printf("\nEnter the element in the list : ");
			scanf("%d",&temp->data);
			if(head==NULL)
			{	
				head=temp;
			}
			else
			{
				temp1=head;
				while(temp1->next!=head)
				{
					temp1=temp1->next;
				}
				temp1->next=temp;
			}
			temp->next=head;
		}
		else
		{
			printf("\nMemory not avilable...node allocation is not possible");
		}
		printf("\nIf you wish to add m ore data on the list enter 1 : ");
		scanf("%d",&choice);
	}while(choice==1);
	
	display(head);
	printf("\nEnter the data of the node which you want to exchange with it's next : ");
	scanf("%d",&key);
	temp=head;
	while(temp->data!=key)
	{
		temp1=temp;
		temp=temp->next;
	}
	if(temp==head)
	{
		temp1=temp->next;
		temp->next=temp1->next;
		temp1->next=temp;
		head=temp1;
	}
	else
	{
		temp2=temp->next;
		temp->next=temp2->next;
		temp2->next=temp;
		temp1->next=temp2;
	}
	
	display(head);
	
	return 0;
}
