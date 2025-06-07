import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        d = {}
        for u,v,w in edges:
            if u not in d:
                d[u] = [[v,w]]
            else:
                d[u] += [[v,w]]
                
        

        weight = [float('inf') for i in range(V)]
        visited = set()
        weight[src] = 0
        curr = src
        li = [[0,src]]
        heapq.heapify(li)
        
        while li:
            curr_dist, curr = heapq.heappop(li)
            if curr in visited:
                continue
            visited.add(curr)
            
            for node , dist in d[curr]:
                if weight[curr] + dist <= weight[node] and node not in visited:
                    weight[node] = weight[curr]+dist
                    heapq.heappush(li , [weight[curr]+dist , node])              
            
            visited.add(curr)
            
            # minnode = -1
            # mindist = float('inf')
            # for i in range(V):
            #     if weight[i]<mindist and i not in visited:
            #         mindist = weight[i]
            #         minnode = i
            # curr = minnode
            # if len(li)==0:
            #     return weight
            # ss = heapq.heappop(li)
            # curr = ss[1]
        return weight