//1)
public class A {
       public static int  findIndex (int[] my_array, int t) {
        if (my_array == null) return -1;
        int len = my_array.length;
        int i = 0;
        while (i < len) 
            if (my_array[i] == t) return i;
            else i=i+1;
        }
        return -1;
    }
    public static void main(String[] args) {
      int[] my_array = {25, 14, 56, 15, 36, 56, 77, 18, 29, 49};
      System.out.println("Index position of 25 is: " + findIndex(my_array, 25));
      System.out.println("Index position of 77 is: " + findIndex(my_array, 77));
       }
}


2)
import java.util.Arrays; 
public class B {
  public static void main(String[] args) 
    {
        int[] my_array = {1, 2, 5, 5, 6, 6, 7, 2};
 
        for (int i = 0; i < my_array.length-1; i++)
        {
            for (int j = i+1; j < my_array.length; j++)
            {
                if ((my_array[i] == my_array[j]) && (i != j))
                {
                    System.out.println("Duplicate Element : "+my_array[j]);
                }
            }
        }
    }    
}

//3)
import java.util.*;
public class C {
   public static void main(String[] args)
    {
      Calendar cal = Calendar.getInstance();
      Date cdate = cal.getTime();
     
      cal.add(Calendar.YEAR, 1); 
      Date nyear = cal.getTime();
     
      cal.add(Calendar.YEAR, -2); 
      Date pyear = cal.getTime();
      System.out.println("\nCurrent Date : " + cdate);
      System.out.println("\nDate before 1 year : " + pyear);
      System.out.println("\nDate after 1 year  : " + nyear+"\n");  	
    }
}
//4)

import java.io.*; 
  
class GFG { 
      
static int R = 5; 
static int C = 5; 
   
static int findMaxSum(int [][]mat) 
{ 
    if (R < 3 || C < 3) 
        return -1; 
  

    for (int i = 0; i < R - 2; i++) 
    { 
        for (int j = 0; j < C - 2; j++) 
        { 
          
            int sum = (mat[i][j] + mat[i][j + 1] +  
                       mat[i][j + 2]) + (mat[i + 1][j + 1]) +  
                       (mat[i + 2][j] + mat[i + 2][j + 1] +  
                       mat[i + 2][j + 2]); 
  
          
            max_sum = Math.max(max_sum, sum); 
        } 
    } 
    return max_sum; 
} 
  

    static public void main (String[] args) 
    { 
        int [][]mat = {{1, 2, 3, 0, 0}, 
                       {0, 0, 0, 0, 0}, 
                       {2, 1, 4, 0, 0}, 
                       {0, 0, 0, 0, 0}, 
                       {1, 1, 0, 1, 0}}; 
        int res = findMaxSum(mat); 
        if (res == -1) 
            System.out.println("Not possible"); 
        else
            System.out.println("Maximum sum of hour glass = "
                                + res); 
    } 
      
} 
