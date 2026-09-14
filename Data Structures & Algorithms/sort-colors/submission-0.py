'''
2   0   2   1   1   0



0   0   1   1   2   2
        i
        z
            t



'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z, t = 0, len(nums) - 1

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[i], nums[z] = nums[z], nums[i]
                z += 1
            if nums[i] == 2:
                nums[i], nums[t] = nums[t], nums[i]
                t -= 1
            if nums[i] == 1 or z > i:
                i += 1
            if i > t:
                break