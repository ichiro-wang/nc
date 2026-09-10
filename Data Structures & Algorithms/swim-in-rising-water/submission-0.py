class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = grid[0][0]
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()
        visit.add((0, 0))

        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            res = max(res, time)
            if r == rows - 1 and c == cols - 1:
                return res
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(minHeap, [grid[nr][nc], nr, nc])