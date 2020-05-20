
3.bubble sort in java
public class bubbleSort{
  public static void main(String a[]){
  int i;
  int array[] = {12,9,4,99,120,1,3,10};
  System.out.println("Values Before the sort:\n");
  for(i = 0; i < array.length; i++)
  System.out.print( array[i]+"  ");
  System.out.println();
  bubble_srt(array, array.length);
  System.out.print("Values after the sort:\n");
  for(i = 0; i <array.length; i++)
  System.out.print(array[i]+"  ");
  System.out.println();
  System.out.println("PAUSE");
  }