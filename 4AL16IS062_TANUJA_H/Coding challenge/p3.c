#include<stdio.h>
#define MAX 1000
void fibonacci(int n)
{
int i, t1 = 0, t2 = 1, nextTerm;
for (i = 1; i<=n; i++)
{
nextTerm = t1 + t2;
t1 = t2;
t2 = nextTerm;
}
printf("%d", t1);
}
void prime(int n)
{
int i, j, flag, count =0;
for (i=2; i<=MAX; i++)
{
flag = 0;
for (j=2; j<i; j++)
{
if(i%j == 0)
{
flag = 1;
break;
}
}
if (flag == 0)
if(++count == n)
{
printf("%d", i);
break;
}
}
}
int main()
{
int n;
scanf("%d", &n);
if(n%2 == 1)
fibonacci (n/2 + 1);
else
prime(n/2);
return 0;
}