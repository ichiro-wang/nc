"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = {}
        nodes[node.val] = Node(node.val)
        q = deque([node])
        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei.val not in nodes:
                    nodes[nei.val] = Node(nei.val)
                    q.append(nei)
                nodes[curr.val].neighbors.append(nodes[nei.val])
        
        return nodes[node.val]