class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0

        for i in range(k + 1):
            newCosts = costs.copy()
            for f, t, p in flights:
                newCosts[t] = min(newCosts[t], costs[f] + p)
            costs = newCosts
        
        return costs[dst] if costs[dst] != float("inf") else -1