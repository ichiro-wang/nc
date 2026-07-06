class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def genPar(openN: int, closeN: int):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                genPar(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                genPar(openN, closeN + 1)
                stack.pop()
        
        genPar(0, 0)
        return res
