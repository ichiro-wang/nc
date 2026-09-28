class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        stack = []
        res = []

        def backtrack(i):
            if i >= len(digits):
                res.append("".join(stack))
                return
            
            digit = digits[i]
            for c in digitMap[digit]:
                stack.append(c)
                backtrack(i + 1)
                stack.pop()
        if digits:
            backtrack(0)
        return res