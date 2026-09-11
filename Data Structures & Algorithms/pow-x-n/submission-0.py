class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = n < 0
        n = abs(n)

        def pow(n, p):
            if p == 0:
                return 1
            if p == 1:
                return n
            res = pow(n, p // 2)
            return res * res * (n if p % 2 else 1)
        
        res = pow(x, n)
        return res if not neg else 1 / res