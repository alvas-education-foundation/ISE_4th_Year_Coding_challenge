#include<stdio.h>

int main()
{
    printf("\n\n\t\tStudytonight - Best place to learn\n\n\n");
    int var;
    int *ptr;
    int **pptr;

    var = 50;


    ptr = &var;

    
    pptr = &ptr;

    printf("\n\nValue of var = %d\n\n", var);

    printf("\n\nValue available at *ptr = %d\n\n", *ptr);

    printf("\n\nValue available at **pptr = %d\n\n", **pptr);

    printf("\n\n\t\t\tCoding is Fun !\n\n\n");
    return 0;
}