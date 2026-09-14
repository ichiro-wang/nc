class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        for p, c in sorted(zip(profits, capital), key=lambda x: x[1]):
            while c > w and k > 0 and maxHeap:
                w -= heapq.heappop(maxHeap)
                k -= 1
            if c <= w:
                heapq.heappush(maxHeap, -p)
        
        while k > 0 and maxHeap:
            w -= heapq.heappop(maxHeap)
            k -= 1
        
        
        return w