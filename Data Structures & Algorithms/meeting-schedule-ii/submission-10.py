"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = Counter([i.start for i in intervals])
        end = Counter([i.end for i in intervals])
        res = 0
        open = close = 0
        s = e = 0

        while s < 100_001:
            while e < s:
                close += end[e]
                e += 1
            res = max(res, open - close)
            open += start[s]
            s += 1
        
        return res
            
