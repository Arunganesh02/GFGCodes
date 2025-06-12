#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        reach = [0]*len(adj)
        short = [0]*len(adj)
        visited = set()
        count = 0
        articulation = set()
        def dfs(node , parent):
            nonlocal reach , short , visited , count , adj , articulation
            
            if node in visited: 
                return 
            count += 1
            reach[node] = count
            short[node] = count
            visited.add(node)
            child = 0
            for i in adj[node]:
                if i == parent : continue
                if i not in visited:
                    dfs(i , node)
                    short[node] = min(short[node] , short[i])
                    if short[i] >= reach[node] and parent != -1:
                        articulation.add(node)
                    child += 1
                    
                else:
                    short[node] = min(short[node] ,reach[i])
                    
            if child>1 and parent == -1:
                articulation.add(node)
        for i in range(len(adj)):
            if i not in visited:
                dfs(i , -1)
        if len(articulation) ==0 : return [-1]
        return sorted(list(articulation))