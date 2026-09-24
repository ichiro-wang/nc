class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, s):
            if i >= len(nums):
                return s
            return backtrack(i + 1, s ^ nums[i]) + backtrack(i + 1, s)
        return backtrack(0, 0)