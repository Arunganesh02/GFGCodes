#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        dist = [float('inf') for i in range(V)]
        dist[src] = 0
        for i in range(V-1):
            for u,v,w in edges:
                if dist[u] + w <= dist[v]:
                    dist[v]  = dist[u] + w
        before = dist.copy()
        for u,v,w in edges:
                if dist[u] + w <= dist[v]:
                    dist[v]  = dist[u] + w
        if dist != before:
            return [-1]
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = 100000000
        return dist