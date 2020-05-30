#include <stdio.h>
int Addrow(int array1[10][10], int k, int c);
int Addcol(int array1[10][10], int k, int r);
 
void main()
{
    int arr[10][10];
    int i, j, row, col, rowsum, colsum, sumall=0;
 
    printf("Enter the order of the matrix \n");
    scanf("%d %d", &row, &col);
    printf("Enter the elements of the matrix \n");
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }
    printf("Input matrix is \n");
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("%3d", arr[i][j]);
        }
        printf("\n");
    }
 
    for (i = 0; i < row; i++)
    {
        rowsum = Addrow(arr, i, col);
        printf("Sum of row %d = %d\n", i + 1, rowsum);
    }
   
    for (j = 0; j < col; j++)
    {
        colsum = Addcol(arr, j, row);
        printf("Sum of column  %d = %d\n", j + 1, colsum);
    }
   
    for (j = 0; j < row; j++)
    {
        sumall = sumall + Addrow(arr, j, col);
    }
    printf("Sum of all elements of matrix = %d\n", sumall);
}

int Addrow(int array1[10][10], int k, int c)
{
    int rsum = 0, i;
    for (i = 0; i < c; i++)
    {
        rsum = rsum + array1[k][i];
    }
    return(rsum);
}
int Addcol(int array1[10][10], int k, int r)
{
    int csum = 0, j;
    for (j = 0; j < r; j++)
    {
        csum = csum + array1[j][k];
    }
    return(csum);
}