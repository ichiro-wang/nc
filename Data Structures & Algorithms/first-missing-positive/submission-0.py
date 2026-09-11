class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        for i in range(len(nums)):
            n = abs(nums[i])
            if n <= len(nums) and nums[n - 1] > 0:
                nums[n - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1