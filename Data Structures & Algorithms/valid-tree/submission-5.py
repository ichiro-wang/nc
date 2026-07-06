class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(a):
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]
        
        def combine(p, q):
            p = find(p)
            q = find(q)

            if p == q:
                return False
            
            nonlocal n
            n -= 1
            
            if rank[p] <= rank[q]:
                parent[p] = q
                rank[q] += rank[p]
            else:
                parent[q] = p
                rank[p] += rank[q]
            
            return True
        
        for p, q in edges:
            if not combine(p, q):
                return False
        
        
        return n == 1