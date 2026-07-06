class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # write your code here
        mirror = {"6":"9","9":"6","8":"8","1":"1","0":"0"}
        res = []
        stack = ["" for i in range(n)]

        def backtrack(l, r):
            if len(stack) > 1 and stack[0] == "0":
                return
            if l > r:
                res.append("".join(stack))
                return
            
            for key, val in mirror.items():
                if l == r and key in ["6", "9"]:
                    continue
                stack[l], stack[r] = key, val
                backtrack(l + 1, r - 1)
        
        backtrack(0, n - 1)
        return res


