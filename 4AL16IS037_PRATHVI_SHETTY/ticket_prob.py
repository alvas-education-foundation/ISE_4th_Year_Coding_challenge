# Given an integer N and an array seats[] where N is the number of people standing in a 
line to buy a movie ticket and seat[i] is the number of empty seats in the ith row of the movie theater. 
The task is to find the maximum amount a theater owner can make by selling movie tickets to N people. 
Price of a ticket is equal to the maximum number of empty seats among all the rows.
def maxAmount(M, N, seats): 
	
	
	q = [] 

	
	for i in range(M): 
		q.append(seats[i]) 

	ticketSold = 0
	ans = 0

	q.sort(reverse = True) 
	while (ticketSold < N and q[0] > 0): 
		ans = ans + q[0] 
		temp = q[0] 
		q = q[1:] 
		q.append(temp - 1) 
		q.sort(reverse = True) 
		ticketSold += 1

	return ans 
if __name__ == '__main__': 
	seats = [1, 2, 4] 
	M = len(seats) 
	N = 3

	print(maxAmount(N, M, seats)) 


