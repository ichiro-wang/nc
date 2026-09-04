"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:
            return root
        curr, left = root, root.left
        temp = left
        while curr and left:
            nxt = curr.right if left == curr.left else curr.left
            left.next = nxt
            left = left.next
            curr = curr.next if left == curr.right else curr
            if not curr:
                curr = temp
                left = temp = temp.left
        
        return root