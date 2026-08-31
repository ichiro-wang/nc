class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0: -1}
        curr = 0

        for i, n in enumerate(nums):
            curr = (curr + n) % k
            if curr in prefix and i - prefix[curr] >= 2:
                return True
            if curr not in prefix:
                prefix[curr] = i
        
        return False
