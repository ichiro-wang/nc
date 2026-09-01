class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.components = n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return
        
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
            self.rank[v] += self.rank[u]
        else:
            self.parent[v] = u
            self.rank[u] += self.rank[v]
        
        self.components -= 1
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u, v in edges:
            dsu.union(u, v)
        
        return dsu.components
        