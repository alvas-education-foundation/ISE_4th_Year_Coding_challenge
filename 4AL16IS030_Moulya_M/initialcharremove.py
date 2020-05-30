# Python3 code to demonstrate 
# Remove Initial character in String List 
# using list comprehension + list slicing 
  
# initializing list 
test_list = ['Amanjeet', 'sakash', 'kakshat', 'Knikhil'] 
  
# printing original list  
print("The original list : " + str(test_list)) 
  
# using list comprehension + list slicing 
# Remove Initial character in String List 
res = [sub[1 : ] for sub in test_list] 
  
# printing result 
print("The list after removing initial characters : " + str(res))