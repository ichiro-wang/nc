class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = 1
        l = 0

        for r in range(1, len(nums)):
            k -= (nums[r] - nums[r - 1]) * (r - l)
            
            while l < r and k < 0:
                k += nums[r] - nums[l]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
