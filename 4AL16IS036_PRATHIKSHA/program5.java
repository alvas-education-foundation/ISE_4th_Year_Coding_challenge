2. b. Write a JAVA Program to demonstrate Exception Handling (Using Nested try catch and finally).
class Prog2b {
static void nestedTry(int a)
{
int sum;
try
{
if(a==1)
a=a/(a-a);
if(a==2)
{
int x[]={2,9};
x[5]=99;
}
}
catch(ArrayIndexOutOfBoundsException e)
{
System.out.println("Array index out of bounds" +e);
}
}
public static void main(String args[]) {
try
{
int a=args.length;
int b=55/a;
System.out.println("No of arguments are = " +a);
nestedTry(a);
}
catch(ArithmeticException e)
{
System.out.println("Divide by zero error" +e);
}
}
}