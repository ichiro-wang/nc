class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        def backtrack(i):
            if i >= len(s):
                res.append(stack.copy())
                return
            
            for j in range(i, len(s)):
                part = s[i:j + 1]
                if not isPali(i, j):
                    continue
                stack.append(part)
                backtrack(j + 1)
                stack.pop()
        
        backtrack(0)
        return res