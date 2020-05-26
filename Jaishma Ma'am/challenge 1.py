@@ -0,0 +1,26 @@
1)
x = input("")
n = int(x)
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


2)
a=input("")
n=int(a)
for i in range(0,n):
    print(i*i)

3)
a = input("")
n1 = int(a)
b = input("")
n2 = int(b)
print(n1 // n2)
print(n1 / n2)
