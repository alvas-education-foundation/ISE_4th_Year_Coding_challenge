# Python3 code to demonstrate working of  
# Remove substring list from String 
# Using loop + replace() 
  
# initializing string 
test_str = "gfg is best for all geeks"
  
# printing original string 
print("The original string is : " + test_str) 
  
# initializing sub list  
sub_list = ["best", "all"] 
  
# Remove substring list from String 
# Using loop + replace() 
for sub in sub_list: 
    test_str = test_str.replace(' ' + sub + ' ', ' ') 
  
# printing result  
print("The string after substring removal : " + test_str) 