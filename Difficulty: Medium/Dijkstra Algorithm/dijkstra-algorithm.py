#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys
import heapq
from typing import List, Tuple


# } Driver Code Ends
class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        # Your code here
        d = {}
        for i in range(len(adj)):
            d[i] = adj[i]

        visited = set()
        current = src
        parent = [-1] * len(adj)
        weight= [float('inf')] * len(adj)
        weight[src] = 0
        
        while True:
            
            for node in d[current]:
                if node[0] not in visited:
                    cu = node[0]
                    if weight[cu] > weight[current] + node[1]  :
                        weight[cu] = weight[current] + node[1]
                        parent[cu] = current
            visited.add(current)   

            indi = -1
            wei = float('inf')
            for i in range(len(weight)):
                if i not in visited and weight[i]<wei:
                    indi = i
                    wei = weight[i]
 
            if indi != -1:
                current = indi
            else:
                break

        return weight
        


#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append((v, w))
            adj[v].append((u, w))
        src = int(input())
        ob = Solution()

        res = ob.dijkstra(adj, src)
        for i in res:
            print(i, end=" ")
        print()
        print("~")
# } Driver Code Ends