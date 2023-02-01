class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        in_bound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        answer = mat[::]
        
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                prefix[r][c] = mat[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]
                
        
        for r in range(m):
            for c in range(n):
                r1, c1 = (min(len(mat) - 1, r + k), min(len(mat[0])-1, c + k))
                r2, c2 = ((max(0, r - k)), max(0, c - k))
                
                answer[r][c] = prefix[r1 + 1][1 + c1]- prefix[r2][c1 + 1] - prefix[r1 + 1][c2] + prefix[r2][c2]
         
                
        return answer