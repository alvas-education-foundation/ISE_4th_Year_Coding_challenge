#Maximize the profit after selling the tickets



def maxProfit(seats, k, n) : 
-
	pq = []; 
	for i in range(k) : 
		pq.append(seats[i]); 
	
	pq.sort(reverse = True); 
	
	
	profit = 0; 

	c = 0; 
	while (c < n) : 
		
		pq.sort(reverse = True); 
		
		top = pq[0]; 
		
		pq.pop(0); 
		
		if (top == 0) : 
			break; 
			
		profit = profit + top; 
		
		pq.append(top - 1); 
		
		
		c += 1; 
	
	return profit; 

if __name__ == "__main__" : 

	seats = [ 2, 3, 4, 5, 1 ]; 
	k = len(seats); 
	n = 6; 

	print(maxProfit(seats, k, n)); 
