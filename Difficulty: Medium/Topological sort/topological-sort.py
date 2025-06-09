class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        d = {i:[] for i in range(V)}
        st = []
        visited = set()
        for u,v in edges:
            d[u] += [v]
            
        def dfs(node):
            nonlocal st,visited
            
            if node in visited:
                return 
            
            for i in d[node] : 
                dfs(i)
            
            st.append(node)
            visited.add(node)
            
            
        for i in range(V):
            dfs(i)
        
        # print(st)
        st.reverse()
        return st