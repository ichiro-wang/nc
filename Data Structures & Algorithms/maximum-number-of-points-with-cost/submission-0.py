"""

points
1   2   3
1   5   1
3   1   1

dp
1   2   3
2   7   4
9   8   7


"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        dp = points[0].copy()

        for r in range(1, rows):
            best = 0
            nextDp = points[r].copy()
            for c in range(cols):
                best = max(best - 1, dp[c])
                nextDp[c] = points[r][c] + best
            best = 0
            for c in range(cols - 1, -1, -1):
                best = max(best - 1, dp[c])
                nextDp[c] = max(nextDp[c], points[r][c] + best)
            dp = nextDp
        
        return max(dp)


