test_list = ['yhxy', 'the', 'basjs'] 

print("The original list : " + str(test_list)) 

res = len(min(test_list, key = len)) 

 
print("Length of minimum string is : " + str(res)) 
