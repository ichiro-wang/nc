class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            m = (l + r) // 2
            curr = 0
            groups = 1
            for n in nums:
                curr += n
                if curr > m:
                    groups += 1
                    curr = n
            if groups <= k:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res