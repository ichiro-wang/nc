# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        n, res = 0, 0
        def dfs(node):
            if not node:
                return

            dfs(node.left)

            nonlocal n, res
            n += 1
            if n == k:
                res = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return res