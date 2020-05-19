#include<stdio.h>
#include<string.h>
int main(){
   char str[25];
   int i;

   printf("Enter the string:");
   scanf("%s",str);

   for(i=0;i<=strlen(str);i++){
      if(str[i]>=97&&str[i]<=122)
         str[i]=str[i]-32;
   }
   printf("\nUpper Case String is: %s",str);
   return 0;
}