# Python3 implementation of SPFA 
from collections import deque 
 
graph = [[] for _ in range(100000)] 

def addEdge(frm, to, weight): 

	graph[frm].append([to, weight]) 

def print_distance(d, V): 
	print("Vertex","\t","Distance from source") 

	for i in range(1, V + 1): 
		print(i,"\t",d[i]) 

def shortestPathFaster(S, V): 

	d = [10**9]*(V + 1) 
 
	inQueue = [False]*(V + 1) 

	d[S] = 0

	q = deque() 
	q.append(S) 
	inQueue[S] = True

	while (len(q) > 0): 
 
		u = q.popleft() 
		inQueue[u] = False

		 
		for i in range(len(graph[u])): 

			v = graph[u][i][0] 
			weight = graph[u][i][1] 

			if (d[v] > d[u] + weight): 
				d[v] = d[u] + weight 


				if (inQueue[v] == False): 
					q.append(v) 
					inQueue[v] = True

	print_distance(d, V) 


if __name__ == '__main__': 
	V = 5
	S = 1

	

	addEdge(1, 2, 1) 
	addEdge(2, 3, 7) 
	addEdge(2, 4, -2) 
	addEdge(1, 3, 8) 
	addEdge(1, 4, 9) 
	addEdge(3, 4, 3) 
	addEdge(2, 5, 3) 
	addEdge(4, 5, -3) 

	
	shortestPathFaster(S, V) 


