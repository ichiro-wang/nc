"""
0x0100
0x0000

0x0010
0x0010

0x0001
0x0011
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        MASK = 0xffffffff
        MAX = 0x7fffffff

        while b:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry
        
        return a if a <= MAX else ~(a ^ MASK)
        