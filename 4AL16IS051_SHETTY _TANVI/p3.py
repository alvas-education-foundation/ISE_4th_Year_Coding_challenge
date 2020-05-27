def findGCDSum(n, a): 
    GCDSum = 0; 
    tempGCD = 0; 
    for i in range(n): 
        for j in range(i, n): 
              
            tempGCD = 0; 
            for k in range(i, j + 1): 
                   
                tempGCD = __gcd(tempGCD, a[k]); 
                  
            GCDSum += tempGCD; 
  
    return GCDSum; 
  
def __gcd(a, b): 
    return a if(b == 0 ) else __gcd(b, a % b);      
  
 
if __name__ == '__main__': 
    n = 5; 
    a = [1, 2, 3, 4, 5]; 
    totalSum = findGCDSum(n, a); 
    print(totalSum); 
   