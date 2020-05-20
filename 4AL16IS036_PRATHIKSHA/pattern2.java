2. Right Triangle Star Pattern

public class Edureka 
{ 
    public static void rightTriangle(int n) 
    { 
        int i, j;  
        for(i=0; i<n; i++) 
 { 
for(j=2*(n-i); j>=0; j--)
        {           
                System.out.print(" ");
            } 
            for(j=0; j<=i; j++) 
            {       
                System.out.print("* ");
            }           
            System.out.println(); 
        } 
    } 
    public static void main(String args[]) 
    { 
        int n = 5; 
        rightTriangle(n); 
    } 
}