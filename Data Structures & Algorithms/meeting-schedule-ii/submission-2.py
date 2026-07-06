"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()

        s, e = 0, 0
        res = 0
        while s < len(start):
            if end[e] <= start[s]:
                e += 1
            else:
                s += 1
            res = max(res, s - e)
        
        return res

