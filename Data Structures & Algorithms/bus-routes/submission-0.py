class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        buses = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                buses[stop].append(i)
        
        visited = set()
        q = deque()
        for bus in buses[source]:
            visited.add(bus)
            q.append([bus, 1])
        
        while q:
            bus, transfers = q.popleft()
            for stop in routes[bus]:
                if stop == target:
                    return transfers
                for b in buses[stop]:
                    if b in visited:
                        continue
                    visited.add(b)
                    q.append([b, transfers + (1 if b != bus else 0)])
        
        return -1