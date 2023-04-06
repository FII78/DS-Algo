from itertools import product 

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j): 
            grid[i][j] = 1 
            closed = 0 < i < m-1 and 0 < j < n-1  
            for nrow, ncol in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] == 0: 
                    closed = dfs(nrow, ncol) and closed 
            return closed 
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i,j):
                        cnt += 1
        return cnt
        # return sum(dfs(i, j) for i, j in product(range(m), range(n)) if grid[i][j] == 0)