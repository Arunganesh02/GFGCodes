#User function Template for python3
from typing import List
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        # Dictionary to store adjacency list
        adj_dict = {i: adj[i] for i in range(V)}

        visited = set()
        span = 0

        # Minimum weights array to keep track of the least edge weight for each vertex
        min_edge = [float('inf')] * V
        min_edge[0] = 0  # Start from node 0

        for _ in range(V):
            # Find the unvisited node with the smallest edge weight
            u = -1
            for i in range(V):
                if i not in visited and (u == -1 or min_edge[i] < min_edge[u]):
                    u = i

            # Include the selected node in the MST
            span += min_edge[u]
            visited.add(u)

            # Update the minimum weights for adjacent vertices
            for neighbor, weight in adj_dict[u]:
                if neighbor not in visited and weight < min_edge[neighbor]:
                    min_edge[neighbor] = weight

        return span

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from typing import List

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))
        print("~")

# } Driver Code Ends