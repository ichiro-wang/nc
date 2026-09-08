'''

2   3   -2  4   -10
                i

res=480
min=-10
max=480

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        MIN = MAX = 1

        for n in nums:
            temp = MIN
            MIN = min(n, n * temp, n * MAX)
            MAX = max(n, n * temp, n * MAX)
            res = max(res, MIN, MAX)
        
        return res
        