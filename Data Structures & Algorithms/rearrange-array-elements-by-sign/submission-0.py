class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos, neg = 0, 1
        for n in nums:
            if n >= 0:
                res[pos] = n
                pos += 2
            else:
                res[neg] = n
                neg += 2
        return res