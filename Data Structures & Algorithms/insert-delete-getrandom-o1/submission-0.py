"""
i = 0 1 2 3
n = 1 5 3 4

1: 0
2: 1 remove
...
5: 1

"""
class RandomizedSet:
    def __init__(self):
        self.stack = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.stack)
        self.stack.append(val)       
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        topVal = self.stack[-1]
        self.stack[index] = topVal
        self.map[topVal] = index
        self.stack.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()