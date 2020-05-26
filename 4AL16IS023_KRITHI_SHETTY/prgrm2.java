import java.util.Scanner;
class DecimalToOctalExample
{
  public static void main(String args[])
  {
    Scanner input = new Scanner( System.in );
    System.out.print("Enter a decimal number : ");
    int num =input.nextInt();
 
    String octalString = Integer.toOctalString(num);
    System.out.println("Method 1: Decimal to octal: " + octalString);
 
    int rem;
 
   
    String str=""; 
 
    char dig[]={'0','1','2','3','4','5','6','7'};
 
    while(num>0)
    {
       rem=num%8; 
       str=dig[rem]+str; 
       num=num/8;
    }
    System.out.println("Method 2: Decimal to octal: "+str);
  }
}