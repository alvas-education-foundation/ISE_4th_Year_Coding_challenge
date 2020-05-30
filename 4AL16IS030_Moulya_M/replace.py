# Python3 code to demonstrate working of 
# Kth word replace in String 
# using split() + join() 
  
# initializing string  
test_str = "GFG is good"
  
# printing original string  
print("The original string is : " + test_str) 
  
# initializing replace string  
rep_str = "best"
  
# initializing K  
K = 1 
  
# Kth word replace in String 
# using split() + join() 
temp = test_str.split(' ') 
res = " ".join(temp[: K]  + [rep_str] + temp[K + 1 :]) 
  
# printing result 
print("The String after performing replace : " + res)