"""

l           k   r
2   1   3   5   4
            p
                i


"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            p = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p < k:
                return quickSelect(p + 1, r)
            if p > k:
                return quickSelect(l, p - 1)
            return nums[p]
        
        l, r = 0, len(nums) - 1
        return quickSelect(l, r)