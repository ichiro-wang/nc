class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            curr = TreeNode(nums[m])
            curr.left = helper(l, m - 1)
            curr.right = helper(m + 1, r)
            return curr
        
        l, r = 0, len(nums) - 1
        return helper(l, r)
