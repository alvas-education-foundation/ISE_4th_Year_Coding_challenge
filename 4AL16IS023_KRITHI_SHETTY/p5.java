5.copping arrays
public class ArrayCopyDemo{
  public static void main(String[] args){
  char[] copyFrom = {'a','b','c','d','e','f','g','h','i','j'};
  char[] copyTo = new char[5];
  System.arraycopy(copyFrom, 2, copyTo, 0, 5);
  System.out.println(new String (copyTo));
  }
} 