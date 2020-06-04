#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node* next;
};

/* Function to insert a node */
void insert_elements(struct node** head, int new_data)
{
    struct node* new_node = (struct node*) malloc(sizeof(struct node));
    new_node -> data = new_data;
    new_node -> next = (*head);
    (*head) = new_node;
}

void display_list(struct node *node)
{
    while (node!=NULL)
    {
        printf(“%d “, node -> data);
        node = node -> next;
    }
}

/* Function to remove duplicates from a sorted list */
void remove_duplicate_elements(struct node *temp)
{
    struct node *ptr1, *ptr2, *duplicate;
    ptr1 = temp;

    while (ptr1 != NULL && ptr1->next != NULL)
    {
        ptr2 = ptr1;

        /* Compare the current element with rest of the elements */
        while (ptr2->next != NULL)
        {
            if (ptr1->data == ptr2->next->data)
            {
                duplicate = ptr2->next;
                ptr2->next = ptr2->next->next;
                delete(duplicate);
            }
            else
                ptr2 = ptr2->next;
        }
        ptr1 = ptr1->next;
    }
}


int main()
{
    struct node* head = NULL;
    int n;
    printf(“\nEnter the total number of elements : “);
    scanf(“%d”, &n);
    printf(“\nEnter the unsorted linked list : “);
    int i;
    for(i = 0; i < n; i++)
    {
        int data;
        scanf(“%d”, &data);
        insert_elements(&head, data);
    }

    printf(“\nLinked list before removing duplicates : “);
    display_list(head);
    printf(“\n”);

    remove_duplicate_elements(head);

    printf(“\nLinked list after removing duplicates : “);
    display_list(head);
    printf(“\n”);


    return 0;
}
-------------------------
2)

#include <bits/stdc++.h> 

using namespace std; 

struct Node { 
	int data; 
	Node *prev, *next; 
}; 


void push(Node** head_ref, int new_data) 
{ 
	Node* new_node = (Node*)malloc(sizeof(struct Node)); 
	new_node->data = new_data; 

	new_node->prev = NULL; 
	new_node->next = (*head_ref); 
	if ((*head_ref) != NULL) 
		(*head_ref)->prev = new_node; 
	(*head_ref) = new_node; 
} 
int digitSum(int num) 
{ 
	int sum = 0; 
	while (num) { 
		sum += (num % 10); 
		num /= 10; 
	} 

	return sum; 
} 
void deleteNode(Node** head_ref, Node* del) 
{ 
	if (*head_ref == NULL || del == NULL) 
		return; 
	if (*head_ref == del) 
		*head_ref = del->next; 

	if (del->next != NULL) 
		del->next->prev = del->prev; 
	if (del->prev != NULL) 
		del->prev->next = del->next; 
	free(del); 

	return; 
} 
 
void deleteEvenDigitSumNodes(Node** head_ref) 
{ 
	Node* ptr = *head_ref; 
	Node* next; 

	// Iterating through the linked list 
	while (ptr != NULL) { 
		next = ptr->next; 
		if (!(digitSum(ptr->data) & 1)) 
			deleteNode(head_ref, ptr); 

		ptr = next; 
	} 
} 

void printList(Node* head) 
{ 
	while (head != NULL) { 
		cout << head->data << " "; 
		head = head->next; 
	} 
} 
int main() 
{ 

	Node* head = NULL; 

	push(&head, 14); 
	push(&head, 9); 
	push(&head, 8); 
	push(&head, 15); 
	push(&head, 18); 

	cout << "Original List: "; 
	printList(head); 

	deleteEvenDigitSumNodes(&head); 

	cout << "\nModified List: "; 
	printList(head); 
} 
----------------------------------
3)
#include "string.h"
#include"iostream"
using namespace std;

bool alphabetcheck(char alphabet){
        if (alphabet >= 'a' && alphabet <= 'z')
            return true;
        return false;
    }
int vowelcheck(char vowel)
{
        if (vowel == 'a' || vowel == 'e' || vowel == 'i' || vowel == 'o' || vowel == 'u')
            return 0;
        return 1;
}

    
int main(void) {
  
    string X = "wayt?arack";  
   
    int XLen = X.size();
    int Arr[2][20];
    memset(Arr, 0, sizeof(Arr[0][0]) * 2 * 20);
    int max0 = 0;
    int max1 = 0;
    int index;
    bool mixed_value = false;
    for (size_t i = 0; i < XLen; i++)
    {
        if (alphabetcheck(X[i]))
        {
            if ((vowelcheck(X[i])) == 0)
            {
                Arr[0][i+1] = Arr[0][i] + 1;
                if (Arr[0][i + 1] > max0)
                    max0 = Arr[0][i + 1]; //check for max 0
                if ((mixed_value == true) && (max0 >= 5) && (Arr[0][i + 1] >= 5)) 
		{
                    if ((i - index >= 5 || (Arr[1][index] + Arr[0][index + 5] == 7)))
                     mixed_value = false;
                }
            }
            else
            {
                Arr[1][i + 1] = Arr[1][i] + 1;
                if (Arr[1][i + 1] > max1)
                    max1 = Arr[1][i + 1]; 
                if (mixed_value == true && max1 >= 3 && Arr[1][i + 1] >= 3 ) 
 
                {
                    if ((i - index >= 3 || (Arr[0][index] + Arr[1][index + 3] == 7)) )
                        mixed_value = false;
                }
            }
            if (mixed_value == false && (max0 >= 5 || max1 >= 3)){
                cout << " BAD " << endl;
                exit(0);
            }
        }
        
        else if (X[i] == '?'){
            Arr[0][i + 1] = Arr[0][i] + 1;
            if (Arr[0][i + 1] > max0)
                max0 = Arr[0][i + 1]; //check for max 1
            Arr[1][i + 1] = Arr[1][i] + 1;
            if (Arr[1][i + 1] > max1)
                max1 = Arr[1][i + 1]; //check for max 1
            index = i;
            mixed_value = true;
        }
    }

    
    if (mixed_value & (max0 >= 5 || max1 >= 3))
        cout << " MIXED " << endl;
    else cout << " GOOD " << endl;
    
    return 0;
}