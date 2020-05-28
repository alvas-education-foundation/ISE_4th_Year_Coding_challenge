3. Write JAVA programs which demonstrates utilities of LinkedList Class
import java.util.*;
import java.io.*;
public class Prog7 {
public static void main(String[] args) {
System.out.println("Linked List Example!");
LinkedList <Integer>list = new LinkedList<Integer>();
int size;
boolean b;
try
{
do
{
System.out.println("1 -> Create list");
System.out.println("2 -> Add element at first");
System.out.println("3 -> Add element at last");
System.out.println("4 -> Add element at specified position");
System.out.println("5 -> Remove element at first");
System.out.println("6 -> Remove element at last");
System.out.println("7 -> Remove element at specified position");
System.out.println("8 -> Display list");
System.out.print("Enter your choice: ");
BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
int ch=Integer.parseInt(br.readLine());
switch(ch)
{
case 1: System.out.println("Enter total no of elements");
int n=Integer.parseInt(br.readLine());
System.out.println("Enter the elements:");
for(int i=0;i<n;i++)
{
int x=Integer.parseInt(br.readLine());
list.add(x);
}
break;
case 8:
if (list.isEmpty())
System.out.println("Linked list is empty");
else
{
System.out.println("Contents of Linked List");
Iterator iterator;
iterator = list.iterator();
while (iterator.hasNext())
System.out.print(iterator.next()+" ");
System.out.println();
System.out.println("First data: " + list.getFirst());
System.out.println("Last data: " + list.getLast());
System.out.println();
10MCA37 JAVA PROGRAMMING LABORATORY
M.S.E.C Dept Of MCA Page 18
}
break;
case 2 : System.out.println("Enter the element:");
int y=Integer.parseInt(br.readLine());
list.addFirst(y);
System.out.println("Now the size of list: " + list.size());
break;
case 3: System.out.println("Enter the element:");
int z=Integer.parseInt(br.readLine());
list.addLast(z);
System.out.println("Now the size of list: " + list.size());
break;
case 4: System.out.println("Enter the position");
int p=Integer.parseInt(br.readLine());
System.out.println("Enter the element:");
int q=Integer.parseInt(br.readLine());
list.add(p,q);
System.out.println("Now the size of list: " + list.size());
break;
case 5:
if (list.isEmpty())
System.out.println("Linked list is empty");
else
{
int first = list.removeFirst();
System.out.println("Data removed from 1st location: " + first);
}
break;
case 6:
if (list.isEmpty())
System.out.println("Linked list is empty");
else
{
int last = list.removeLast();
System.out.println("Data removed from last location: " + last);
System.out.print("Now the list contain: ");
}
break;
case 7:
if (list.isEmpty())
System.out.println("Linked list is empty");
else
{
System.out.println("Enter the position");
int v=Integer.parseInt(br.readLine());
int second = list.remove(v);
System.out.println("Data removed from 2nd location: " + second);
}
break;
default : System.out.println("Invalid choice");
10MCA37 JAVA PROGRAMMING LABORATORY
M.S.E.C Dept Of MCA Page 19
}
b=(ch<9);
}while(b);
}
catch(IOException e)
{
System.out.println("Error " +e);
}
}
}