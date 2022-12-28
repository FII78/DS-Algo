class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        distance = [[float("inf")] * n for _ in range(m)]
        distance[0][0] = 0
        heap = [(0, 0, 0)]
        DIR = [(0,1),(1,0),(-1,0),(0,-1)]
        inbound = lambda x,y: 0 <= x < m and 0 <= y < n
        
        while heap:
            d, r, c = heappop(heap)
            if d < distance[r][c]:
                continue
            
            if r == m-1 and c == n-1:
                return d
            
            for x,y in DIR:
                nr, nc = r+x, c+y
                if inbound(nr, nc):
                    newD = max(d, abs(heights[nr][nc]-heights[r][c]))
                    if newD < distance[nr][nc]:
                        distance[nr][nc] = newD
                        heappush(heap, (distance[nr][nc], nr, nc))
        
        