class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = ["0"] * len(s)
        count = 0
        for c in s:
            count += (1 if c == "1" else 0)
        
        for i in range(count - 1):
            res[i] = "1"
        
        res[-1] = "1" if count > 0 else "0"

        return "".join(res)