class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        inbound = lambda x,y: 0 <= x < n and 0 <= y < m
        def dfs(r,c):
            if not inbound(r,c):
                return float("inf")
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0

            top = dfs(r + 1,c)
            bottom = dfs(r - 1,c)
            right = dfs(r,c + 1)
            left = dfs(r,c - 1)

            return top + bottom + right + left + 1
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = dfs(i,j)
                    if ans != float("inf"):
                        count += ans

        return count


        
        