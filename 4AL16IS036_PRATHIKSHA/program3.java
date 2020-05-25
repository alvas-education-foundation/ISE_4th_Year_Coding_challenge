1. b. Write a JAVA Program to implement Inner class and demonstrate its Access Protections.
class OuterClass
{
int a[]=new int[10];
int sum=0,i,k=0;
void initialize()
{
System.out.println("Inside Outer class method");
for(i=0;i<10;i++)
{
a[i]=k;
k++;
}
System.out.println("Array Elements are");
for(i=0;i<10;i++)
System.out.print(" " +a[i]);
System.out.println();
}
void show()
{
InnerClass ob=new InnerClass();
ob.cal();
}
class InnerClass
{
void cal()
{
System.out.println("Inside Inner class method");
for(i=0;i<10;i++)
sum+=a[i];
System.out.println("Sum :" +sum);
}
}
}
class Prog1b
{
public static void main(String args[])
{
OuterClass ob1=new OuterClass();
ob1.initialize();
ob1.show();
}
}
