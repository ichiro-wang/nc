class Solution:

    def __init__(self, w: List[int]):
        self.prob = [0]
        for n in w:
            self.prob.append(self.prob[-1] + n)

    def pickIndex(self) -> int:
        target = self.prob[-1] * random.random()
        l, r = 0, len(self.prob) - 1
        res = -1
        while l < r:
            m = (l + r) // 2
            if self.prob[m] <= target:
                l = m + 1
                res = m
            else:
                r = m
        
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()