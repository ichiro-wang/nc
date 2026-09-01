"""
5

    1   2   5
0   1   1   1
1   1   1   1
2   1   
3
4
5

"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * len(coins) for i in range(amount + 1)]
        dp[0] = [1] * len(coins)

        for amt in range(1, amount + 1):
            for i in range(len(coins)):
                if i > 0:
                    dp[amt][i] = dp[amt][i - 1]
                rem = amt - coins[i]
                if rem < 0:
                    continue
                dp[amt][i] += dp[rem][i]
        
        return dp[-1][-1]