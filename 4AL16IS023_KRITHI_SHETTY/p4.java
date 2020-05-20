
4.convert array into array list
import java.util.*;
public class ConvertArrayToArrayList {
 public static void main(String args[]) {
  String[] states= {"UP", "Bihar", "Kolkata", "Delhi"};
  List stateslist = new Arrays(Arrays.asList(states));
  System.out.println("ArrayList of states: " + stateslist);
 }
}

