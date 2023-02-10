class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque([])
        
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
                    visited.add((i,j))
        
        if len(queue) == 0 or len(queue) == (len(grid)*len(grid)):
            return -1
        DIR = [[-1,0],[0,-1],[1,0],[0,1]]
        level = 0
        
        while queue:
            i, j, d = queue.popleft()
            level += d > level
          
            for x,y in DIR:
                nx = i + x
                ny = j + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx,ny) not in visited:
                    queue.append((nx, ny,level+1))
                    visited.add((nx,ny))
    
        return level 
                        
                    
                        
            
            
            
            
                    
                    
        