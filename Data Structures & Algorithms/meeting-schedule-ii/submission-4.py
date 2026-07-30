"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res = 0
        s = e = 0

        while s < len(start):
            while e < len(end) and end[e] <= start[s]:
                e += 1
            res = max(res, s - e + 1)
            s += 1
        
        return max(res, s - e)