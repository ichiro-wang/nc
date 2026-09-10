'''

10

1,0 2,2

2   1   5   6   2   3
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, (i - index) * height)
            stack.append([index, h])
        
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
        
        return res
