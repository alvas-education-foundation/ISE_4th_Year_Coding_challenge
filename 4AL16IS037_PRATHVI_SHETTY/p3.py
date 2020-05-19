#selection sort

for i in range(len(A)): 
      
   
    min_index = i 
    for j in range(i+1, len(A)): 
        if A[min_index] > A[j]: 
            min_index = j 
              
           
    A[i], A[min_index] = A[min_index], A[i] 
  
A = [45,78,65,43] 
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i]),







