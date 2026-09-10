class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(deque)
        for f, t in tickets:
            adj[f].append(t)
        
        res = deque()
        def dfs(src):
            while adj[src]:
                nxt = adj[src].popleft()
                dfs(nxt)
            res.appendleft(src)
        
        dfs("JFK")
        return list(res)
                