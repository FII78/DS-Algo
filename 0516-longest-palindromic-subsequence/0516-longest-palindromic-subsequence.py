class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s2 = s[::-1]

        grid = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for row in range(1, n + 1):
            for col in range(1, n + 1):
                if s2[col - 1] == s[row - 1]:
                    grid[row][col] = grid[row-1][col-1] + 1
                else:
                    grid[row][col] = max(grid[row-1][col],grid[row][col-1])       
                        
        return grid[n][n]