class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = {}
        for i, c in enumerate(s):
            end[c] = i
        res = []
        l = 0
        target = 0
        for r in range(len(s)):
            target = max(target, end[s[r]])
            if r == target:
                res.append(r - l + 1)
                l = r + 1
        return res