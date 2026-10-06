# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [None]
        curr = root
        res = []
        while curr:
            if curr.left:
                stack.append(curr)
                left = curr.left
                curr.left = None
                curr = left
            elif curr.right:
                stack.append(curr)
                right = curr.right
                curr.right = None
                curr = right
            else:
                res.append(curr.val)
                curr = stack.pop()
        
        return res


                    