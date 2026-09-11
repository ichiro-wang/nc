class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        
        visit = set()
        cycle = set()
        res = []
        
        def dfs(a):
            if a in cycle:
                return False
            if a in visit:
                return True
            
            cycle.add(a)
            visit.add(a)

            for b in adj[a]:
                if not dfs(b):
                    return False
            
            res.append(a)
            adj[a] = []
            cycle.remove(a)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res