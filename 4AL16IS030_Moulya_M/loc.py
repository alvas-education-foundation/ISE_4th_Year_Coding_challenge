# Python3 code to demonstrate working of  
# Word location in String 
# Using findall() + index() 
import re 
  
# initializing string 
test_str = 'geeksforgeeks is best for geeks'
  
# printing original string 
print("The original string is : " + test_str) 
  
# initializing word  
wrd = 'best'
  
# Word location in String 
# Using findall() + index() 
test_str = test_str.split() 
res = -1
for idx in test_str: 
    if len(re.findall(wrd, idx)) > 0: 
        res = test_str.index(idx) + 1
  
# printing result  
print("The location of word is : " + str(res))