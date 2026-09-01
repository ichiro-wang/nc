class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for i in range(len(coins) + 1)]
        for i in range(len(coins)):
            dp[i][0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                diff = j - coins[i]
                dp[i][j] = dp[i + 1][j] + (dp[i][diff] if diff >= 0 else 0)
        
        return dp[0][amount]