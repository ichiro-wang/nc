class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        res = []
        adj = defaultdict(deque)
        for f, t in tickets:
            adj[f].append(t)

        def dfs(f):
            while adj[f]:
                t = adj[f].popleft()
                dfs(t)
            res.append(f)

        dfs("JFK")
        res.reverse()
        return res