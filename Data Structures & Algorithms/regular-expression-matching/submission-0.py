"""

    a   a   b   '
a   T   T   T   F
*   F   F   F   F
b   F   F   T   F
'   F   F   F   T

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for i in range(len(p) + 1)]
        dp[-1][-1] = True

        for i in range(len(p) - 1, -1, -1):
            for j in range(len(s), -1, -1):
                matches = j < len(s) and (p[i] == s[j] or p[i] == ".")
                if i + 1 < len(p) and p[i + 1] == "*":
                    dp[i][j] = dp[i + 2][j] or (dp[i][j + 1] if matches else False)
                elif matches:
                    dp[i][j] = dp[i + 1][j + 1]
        
        return dp[0][0]
        