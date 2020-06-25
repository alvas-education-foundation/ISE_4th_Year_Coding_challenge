1).  Write a python program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print( ",".join(items))


2). Write a python program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.


value = input("Enter value: ")

n1 = value * 1
n2 = value * 2
n3 = value * 3
n4 = value * 4

total = int(n1) + int(n2) + int(n3) + int(n4)
print(total)



3).A website requires the users to input username and password to register. 
Write a python program to check the validity of password input by users.


import re
passwords = input("Type in: ")
passwords = passwords.split(",")
accepted_pass = []
for i in passwords:
    
    if len(i) < 6 or len(i) > 12:
        continue

    elif not re.search("([a-z])+", i):
        continue

    elif not re.search("([A-Z])+", i):
        continue

    elif not re.search("([0-9])+", i):
        continue

    elif not re.search("([!@$%^&])+", i):
        continue

    else:
        accepted_pass.append(i)

print((" ").join(accepted_pass))