1)Task
You are given the year, and you have to write a function to check if the year is leap or not.
Input Format
Read y, the year that needs to be checked.
Constraints
1900<=y <= 105
Output Format
Output is taken care of by the template. Your function must return a boolean value (True/False)
Sample Input 0
1990
Sample Output 0
False

def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_leap(int(input())))

2)Read two integers from STDIN and print three lines where:
1.The first line contains the sum of the two numbers.
2.The second line contains the difference of the two numbers (first - second).
3.The third line contains the product of the two numbers.
Input Format
The first line contains the first integer,a . The second line contains the second integer,b .
Constraints
1<=a <= 1010
1<=b <= 1010
Output Format
Print the three lines as explained above.
Sample Input 0
2
3

ans:
a = int(input())                         
b = int(input())
if 1<=a<=10**10 and 1<=b<=10**10:         
sum = a+b
difference = a-b
product = a*b
print (sum)                              
print (difference)                     
print (product) 


3) Read an integer  N.
Without using any string methods, try to print the following:
 1 2 3 ….. N
Note that “ …..” represents the values in between.
Input Format
The first line contains an integer  N.
Output Format
Output the answer as explained in the task.
Sample Input 0
3
Sample Output 0
123

from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    list = []
    num = 1
    string = "" 
    for x in range(n):
        list.append(num)
        num += 1
    for x in list:
        string += str(x)
    print(string)