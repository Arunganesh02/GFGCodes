from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        d = {i:[] for i in range(V)}

        sumi = 0
        for i in range(len(adj)):
            for v,w in adj[i]:
                d[i] += [[v,w]]
                d[v] += [[i,w]]
        
        li = [[0,0]]
        heapq.heapify(li)
        visited = set()
        sumi  = 0
        
        while(len(li) != 0):
            wei , node = heapq.heappop(li)
            if node in visited : 
                continue
            
            sumi += wei
            visited.add(node)
            
            for node , weight in d[node]:
                if node not in visited:
                    heapq.heappush(li , [weight , node])
                    
                
        return sumi    