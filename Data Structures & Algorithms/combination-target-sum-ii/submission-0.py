class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []
        stack = []

        def dfs(i, sum):
            if sum == target:
                res.append(stack.copy())
                return
            if i >= len(nums) or sum > target:
                return
            stack.append(nums[i])
            dfs(i + 1, sum + nums[i])

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            stack.pop()
            dfs(i + 1, sum)
        
        dfs(0, 0)
        return res