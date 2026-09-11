'''

size=3

2   4   3

'''
class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        self.map = {}
        self.cap = capacity

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        node.prev = node.next = None
        self.cap += 1
        del self.map[node.key]

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next
        self.cap -= 1
        self.map[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
        else:
            node = Node(key, value)
        
        self.insert(node)

        if self.cap < 0:
            lru = self.left.next
            self.remove(lru)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)