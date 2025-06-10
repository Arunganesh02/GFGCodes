#User function Template for python3
class DisjointSet:
    def __init__(self,n):
        self.size = [1]*(n+1)
        self.parent = [0]*(n+1)
        
        for i in range(n+1):
            self.parent[i] = i
            
    def findupar(self,u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.findupar(self.parent[u])
        return self.parent[u]
        
    def unionBySize(self,u,v):
        parU = self.findupar(u)
        parV = self.findupar(v)
        
        if parU == parV : return
        
        if self.size[parV] > self.size[parU]:
            self.parent[parU] = self.parent[parV]
            self.size[parV] += self.size[parU]
        else:
            self.parent[parV] = self.parent[parU]
            self.size[parU] += self.size[parV]
class Solution:
    def Solve(self, n, adj):
        # Code here
        ds = DisjointSet(n-1)
        c = 0

        for u,v in adj:
            if ds.findupar(u) != ds.findupar(v):
                ds.unionBySize(u,v)

            else: c+=1
        uni = 0
        # print(ds.parent)
        for i in range(n):
            if ds.findupar(i) == i : uni +=1
        if uni-1 > c : return -1
        elif uni == 1 : return 0
        return uni-1
        
        
        