2. a. Write a JAVA Program to demonstrate Inheritance.
class SuperClass
{
int a,b;
SuperClass(int x,int y)
{
a=x;
b=y;
}
void show()
{
System.out.println("In Super Class");
System.out.println(" A and B are " + a + " " + b);
}
}
class SubClass extends SuperClass
{
int ans;
int add;
SubClass(int a,int b,int c)
{
super(a,b);
ans=c;
}
void show()
{
System.out.println("In Sub Class");
System.out.println("C value is: " + ans);
super.show();
add=a+b+ans;
System.out.println("Addition of A B and C :" + add);
}
}
class Prog2a
{
public static void main(String args[])
{
SubClass ob=new SubClass(10,20,30);
ob.show();
}
}
OUTPUT:
In sub class
C value is : 30
In Super class
A and B are 10 and 20
Addition of A B and C : 60


