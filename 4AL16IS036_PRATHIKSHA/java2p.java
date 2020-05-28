  Java Program to Convert Binary Code of a Number into its Equivalent Gray’s Code Without Using Recursio

 import static java.lang.StrictMath.pow;

    import java.util.Scanner;

    public class Binary_Gray 

    {

        public static void main(String[] args) 

        {

            int a, b, x, result = 0, i = 0;

            Scanner s = new Scanner(System.in);

            System.out.print("Enter Binary number:");

            x = s.nextInt();

            while(x != 0)

            {

                a = x % 10;

                x = x / 10;

                b = x % 10;

                if((a & ~ b) == 1 || (~ a & b) == 1)

                {

                    result = (int) (result + pow(10,i));

                }

                i++;

            }

            System.out.println("Gray Code:"+result);

        }

    }