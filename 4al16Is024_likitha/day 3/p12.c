#include <stdio.h>

int main()
{
    printf("\n\n\t\tStudytonight - Best place to learn\n\n\n");

    char str[100];
    char rev[100];
    char *sptr = str; 
    char *rptr = rev; 

    int i = -1;

    printf("\n\nEnter a string: ");
    scanf("%s", str);

   
    while(*sptr)
    {
        sptr++;
        i++; 
    }

    while(i >= 0)
    {
        /
        sptr--; 
        *rptr = *sptr;  
        rptr++; 
        i--;   
    }
    
    *rptr = '\0'; 
    rptr = rev;

    while(*rptr)
    {
        *sptr = *rptr;
        sptr++;
        rptr++;
    }

    printf("\n\nReverse of the string is: %s ", str);
    printf("\n\n\t\t\tCoding is Fun !\n\n\n");
    return 0;
}