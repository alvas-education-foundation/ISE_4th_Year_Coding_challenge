//1)
class ArmstrongExample{  
  public static void main(String[] args)  {  
    int c=0,a,temp;  
    int n=153;//It is the number to check armstrong  
    temp=n;  
    while(n>0)  
    {  
    a=n%10;  
    n=n/10;  
    c=c+(a*a*a);  
    }  
    if(temp==c)  
    System.out.println("armstrong number");   
    else  
        System.out.println("Not armstrong number");   
   }  
}  
//2)
public class c1  
{ 
    static final int NO_OF_CHARS = 256; 
      
    
    static char getSecondMostFreq(String str) 
    { 
         
        int[] count = new int[NO_OF_CHARS]; 
        int i; 
        for (i=0; i< str.length(); i++) 
            (count[str.charAt(i)])++; 
       
         
        int first = 0, second = 0; 
        for (i = 0; i < NO_OF_CHARS; i++) 
        { 
            /* If current element is smaller than 
            first then update both first and second */
            if (count[i] > count[first]) 
            { 
                second = first; 
                first = i; 
            } 
       
            
            else if (count[i] > count[second] && 
                     count[i] != count[first]) 
                second = i; 
        } 
       
        return (char)second; 
    } 
     public static void main(String args[]) 
    { 
      String str = "geeksforgeeks"; 
      char res = getSecondMostFreq(str); 
      if (res != '\0') 
         System.out.println("Second most frequent char"+ 
                                       " is " + res); 
      else
         System.out.println("No second most frequent"+ 
                                       "character"); 
    } 
}

//3)
import java.util.HashSet;
public class Exercise34 {    
   public static void main(String[] args) {
        int nums[] = {49, 1, 3, 200, 2, 4, 70, 5};  
		System.out.println("Original array length: "+nums.length);
		System.out.print("Array elements are: ");
       for (int i = 0; i < nums.length; i++)
        {
            System.out.print(nums[i]+" ");
        }
		System.out.println("\nThe new length of the array is: "+longest_sequence(nums));
			
    }
    
    public static int longest_sequence(int[] nums) {
      final HashSet<Integer> h_set = new HashSet<Integer>();
        for (int i : nums) h_set.add(i);

        int longest_sequence_len = 0;
        for (int i : nums) {
            int length = 1;
            for (int j = i - 1; h_set.contains(j); --j) {
                h_set.remove(j);
                ++length;
            }
            for (int j = i + 1; h_set.contains(j); ++j) {
                h_set.remove(j);
                ++length;
            }
            longest_sequence_len = Math.max(longest_sequence_len, length);
        }
        return longest_sequence_len;
    }
}

//4)
import java.util.*;
import java.lang.*;
public class Main
{
   public static void main (String[] args) 
    {  
        int nums[] = {0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1};
        int i,  nums_size = nums.length;
        int left = 0, right = nums_size - 1;
        
        System.out.println("Original Array : "+Arrays.toString(nums));  
 
        while (left < right) 
        {
           
            while (nums[left] == 0 && left < right)
               left++;
 
            
            while (nums[right] == 1 && left < right)
                right--;
 
           
            if (left < right) 
            {
                nums[left] = 0;
                nums[right] = 1;
                left++;
                right--;
            }
        }
        
       System.out.println("Array after segregation is : "+Arrays.toString(nums));  
    }
}