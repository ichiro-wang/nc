class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]

        for row in range(1, rowIndex + 1):
            newDp = [0] * (row + 1)
            for i in range(len(dp)):
                newDp[i] += dp[i]
                newDp[i + 1] += dp[i]
            dp = newDp
        
        return dp