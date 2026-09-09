from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.keys[key]
        i = bisect_right(values, [timestamp, chr(ord('z') + 1)]) - 1
        return values[i][1] if i >= 0 else ""