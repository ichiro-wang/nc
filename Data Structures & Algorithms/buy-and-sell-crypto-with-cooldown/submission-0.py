"""
1   2   3   0   2

0   0   2   2   -2   0
0   0   0   0   2   0
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {buying: [0] * (len(prices) + 1) for buying in [True, False]}

        for i in range(len(prices) - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = -prices[i] + dp[not buying][i + 1]
                    cool = dp[buying][i + 1]
                    dp[buying][i] = max(buy, cool)
                else:
                    sell = prices[i] + (dp[not buying][i + 2] if i + 2 < len(prices) + 1 else 0)
                    cool = dp[buying][i + 1]
                    dp[buying][i] = max(sell, cool)
        
        return dp[True][0]
        


        dp = {}

        def dfs(i, t):
            if i >= len(prices):
                return 0
            if (i, t) in dp:
                return dp[(i, t)]
            
            if t == "buy":
                do = dfs(i + 1, "sell") - prices[i]
                cool = dfs(i + 1, "buy")
            else:
                do = dfs(i + 2, "buy") + prices[i]
                cool = dfs(i + 1, "sell")
            
            dp[(i, t)] = max(do, cool)
            return dp[(i, t)]
        
        return dfs(0, "buy")
        