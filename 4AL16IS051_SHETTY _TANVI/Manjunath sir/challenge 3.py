1).
#include <stdio.h> 
  int findStep(int n) 
{ 
    if (n == 1 || n == 0) 
        return 1; 
    else if (n == 2) 
        return 2; 
  
    else
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1); 
} 
  
int main() 
{ 
    int n = 4; 
    printf("%d\n", findStep(n)); 
    return 0; 
} 




2).
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
def doOverlap(l1, r1, l2, r2): 
       
    if(l1.x >= r2.x or l2.x >= r1.x): 
        return False
   if(l1.y <= r2.y or l2.y <= r1.y): 
        return False
       return True
  if __name__ == "__main__": 
    l1 = Point(0, 10) 
    r1 = Point(10, 0) 
    l2 = Point(5, 5) 
    r2 = Point(15, 0) 
  
    if(doOverlap(l1, r1, l2, r2)): 
        print("Rectangles Overlap") 
    else: 
        print("Rectangles Don't Overlap") 
  
3).

#include <stdio.h> 
  
int getMissingNo(int a[], int n) 
{ 
    int i, total; 
    total = (n + 1) * (n + 2) / 2; 
    for (i = 0; i < n; i++) 
        total -= a[i]; 
    return total; 
} 
  
int main() 
{ 
    int a[] = { 1, 2, 4, 5, 6 }; 
    int miss = getMissingNo(a, 5); 
    printf("%d", miss); 
    getchar(); 
} 
