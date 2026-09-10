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

        subsets = set([0])
        for n in nums:
            newSubsets = subsets.copy()
            for s in subsets:
                if s + n > target:
                    continue
                if s + n == target:
                    return True
                newSubsets.add(s + n)
            subsets = newSubsets
        
        return False