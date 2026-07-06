class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            pu, pv = find(u), find(v)

            if pu == pv:
                return
            if rank[pu] < rank[pv]:
                rank[pv] += rank[pu]
                parent[pu] = pv
            else:
                rank[pu] += rank[pv]
                parent[pv] = pu
        
        for e1, e2 in edges:
            if find(e1) == find(e2):
                return False
            union(e1, e2)
            
        print(parent, rank)

        for i in range(len(parent) - 1):
            if parent[i] != parent[i + 1]:
                return False
        return True