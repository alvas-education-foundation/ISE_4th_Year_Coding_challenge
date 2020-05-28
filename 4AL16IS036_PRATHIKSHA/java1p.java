  
Java Program to Put Even & Odd Elements of an Array in 2 Separate Arrays


  import java.util.Scanner;

    public class Even_Odd

    {

        public static void main(String[] args) 

        {

            int n, j = 0, k = 0;

            Scanner s = new Scanner(System.in);

            System.out.print("Enter no. of elements you want in array:");

            n = s.nextInt();

            int a[] = new int[n];

            int odd[] = new int[n];

            int even[] = new int[n];

            System.out.println("Enter all the elements:");

            for(int i = 0; i < n; i++)

            {

                a[i] = s.nextInt();

            }

            for(int i = 0; i < n; i++)

            {

                if(a[i] % 2 != 0)

                {

                    odd[j] = a[i];

                    j++;

                }

                else

                {

                    even[k] = a[i];

                    k++;

                }

            }

            System.out.print("Odd:");

            if(j > 1)

            {

                for(int i = 0;i < (j-1); i++)

                {

                    System.out.print(odd[i]+",");

                }

                System.out.print(odd[j-1]);

            }

            else

            {

                System.out.println("No number");

            }

            System.out.println("");

            System.out.print("Even:");

            if(k > 1)

            {

                for(int i = 0; i < (k-1); i++)

                {

                    System.out.print(even[i]+",");

                }

            System.out.print(even[k-1]);

            }

            else

            {

                System.out.println("No number");

            }

        }

    }