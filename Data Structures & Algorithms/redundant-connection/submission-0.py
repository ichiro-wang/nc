class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return False
        if self.size[u] < self.size[v]:
            self.size[v] += self.size[u]
            self.parent[u] = v
        else:
            self.size[u] += self.size[v]
            self.parent[v] = u
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        
        return [-1, -1]
        