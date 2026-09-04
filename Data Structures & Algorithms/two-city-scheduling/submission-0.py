class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs = sorted(costs, key=lambda x: x[0] - x[1])

        res = 0
        for i in range(len(costs)):
            if i < n:
                res += costs[i][0]
            else:
                res += costs[i][1]
        
        return res
            