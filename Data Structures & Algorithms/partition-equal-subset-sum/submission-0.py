'''

1   2   3   4

total=10
target=5
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if target * 2 != total:
            return False
        
        dp = {}
        def backtrack(i, s):
            if (i, s) in dp:
                return dp[(i, s)]
            if s == target:
                return True
            if s > target or i >= len(nums):
                return False
            res = backtrack(i + 1, s + nums[i]) or backtrack(i + 1, s)
            dp[(i, s)] = res
            return res
        
        return backtrack(0, 0)
        