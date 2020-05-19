2.two dimensional array in java
public class Twodarray {
    public static void main(String args[]){
       int a[][]=new int[5][4]; //An array with 5 row and 4 coloumn.
       for(int i=0;i<a.length;i++) 
       {
           for(int j=0;j<a[i].length;j++)
            {
           a[i][j]=i;
           System.out.print(" " +a[i][j]);
              }
           System.out.println(" ");
          }
        }
       }