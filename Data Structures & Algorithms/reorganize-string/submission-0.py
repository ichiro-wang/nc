class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        res = []

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            if res and res[-1] == char:
                if not maxHeap:
                    return ""
                nextCnt, nextChar = heapq.heappop(maxHeap)
                res.append(nextChar)
                if nextCnt < -1:
                    heapq.heappush(maxHeap, [nextCnt + 1, nextChar])
                cnt -= 1
            else:
                res.append(char)
            if cnt < -1:
                heapq.heappush(maxHeap, [cnt + 1, char])
        
        return "".join(res)