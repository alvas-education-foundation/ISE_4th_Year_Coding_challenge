#include<stdio.h>

int func(int a, int b) 
{
    printf("\n\n a = %d \n", a);
    printf("\n\n b = %d \n", b);
}

int main()
{
    printf("\n\n\t\tStudytonight - Best place to learn\n\n\n");

    // function pointer
    int(*fptr)(int , int);

    // assign address to function pointer
    fptr = func;

    // function calling
    func(2,3);
    fptr(2,3);  // calling a function referring to pointer to a function

    printf("\n\n\t\t\tCoding is Fun !\n\n\n");
    return 0;
}