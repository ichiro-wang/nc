class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helper(nums, 0, len(nums) - 1), self.helper(nums, 1, len(nums)), nums[0])
    
    def helper(self, nums, l, r):
        dp1, dp2 = 0, 0
        for i in range(l, r):
            curr = max(dp1 + nums[i], dp2)
            dp1, dp2 = dp2, curr
        return dp2