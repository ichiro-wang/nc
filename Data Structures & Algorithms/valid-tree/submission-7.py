class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(p):
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]
        
        def combine(p, q):
            p = find(p)
            q = find(q)

            if p == q:
                return False
            
            if rank[p] < rank[q]:
                parent[p] = parent[q]
                rank[q] += rank[p]
            else:
                parent[q] = parent[p]
                rank[p] += rank[q]
            
            return True
        
        for p, q in edges:
            if not combine(p, q):
                return False
        
        return True