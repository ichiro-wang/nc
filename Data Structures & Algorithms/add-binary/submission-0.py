class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry = 0
        res = []
        base = 2
        
        for i in range(max(len(a), len(b))):
            va = int(a[i]) if i < len(a) else 0
            vb = int(b[i]) if i < len(b) else 0

            v = va + vb + carry
            carry = v // base
            v = v % base

            res.append(str(v))
        
        if carry:
            res.append(str(carry))
        
        return "".join(res[::-1])