class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for f, t, p in flights:
            adj[f].append([t, p])
        prices = [float("inf")] * n
        prices[src] = 0

        q = deque([[src, 0, 0]])
        while q:
            src, cst, hops = q.popleft()
            if hops > k:
                continue
            for nxt, w in adj[src]:
                nextCst = cst + w
                if nextCst < prices[nxt]:
                    prices[nxt] = nextCst
                    q.append([nxt, nextCst, hops + 1])
        
        return prices[dst] if prices[dst] != float("inf") else -1