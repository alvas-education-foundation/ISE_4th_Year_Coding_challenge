Java program to sort an array of integers in ascending order using Arrays.sort() method.

import java.util.Arrays;
 
public class JavaSortExample 
{    
    public static void main(String[] args) 
    {
        //Unsorted array
        Integer[] numbers = new Integer[] { 15, 11, 9, 55, 47, 18, 520, 1123, 366, 420 };
         
        //Sort the array
        Arrays.sort(numbers);
         
        //Print array to confirm
        System.out.println(Arrays.toString(numbers));
    }
}