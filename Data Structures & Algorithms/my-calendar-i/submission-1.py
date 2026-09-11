import bisect
class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        curr = [startTime, endTime]
        i = bisect.bisect_left(self.bookings, curr)
        if i < len(self.bookings) and self.bookings[i][0] < endTime:
            return False
        if i > 0 and self.bookings[i - 1][1] > startTime:
            return False
        self.bookings.insert(i, curr)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)