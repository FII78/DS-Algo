class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        n = len(grid)
        
        DIR = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        queue = deque()
        queue.append((0,0))
        
        visited = set()
        visited.add((0,0))
                                                 
            
        level = 1
        
        while queue:
            for _ in range(len(queue)):
                r, c  = queue.popleft()
                
                if r == n-1 and c == n-1:
                    return level
                
                for x,y in DIR:
                    nr = x + r
                    nc = y + c
                    
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            level += 1
        return -1
    
        
     