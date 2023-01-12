class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        start_row,start_col = 0,0
        end_row,end_col = 0,0
        empty_cell = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_row,start_col = i,j
                elif grid[i][j] == 2:
                    end_row,end_col = i,j
                elif grid[i][j] == 0:
                    empty_cell += 1
        
        visited = set()
        output = 0
        inbound = lambda x,y: 0 <= x < m and 0 <= y < n
        DIR = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r,c,visited,walk):
            nonlocal output
            if r == end_row and c == end_col:
                if walk == empty_cell + 1:
                    output += 1
                return
            if inbound(r,c) and grid[r][c] != -1 and (r,c) not in visited:
                visited.add((r,c))
                for i,j in DIR:
                    dfs(r + i,c + j,visited,walk+1)
                visited.remove((r,c))
        dfs(start_row,start_col,visited,0)

        return output