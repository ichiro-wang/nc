"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedIntervals = sorted(intervals, key=lambda x: x.start)

        for i, s in enumerate(sortedIntervals):
            if i == 0:
                continue
            if s.start < sortedIntervals[i - 1].end:
                return False
            
        return True
