class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l = 0
        r = int(sqrt(c))
        print(r)
        
        while l <= r:
            ans = l ** 2 + r ** 2
            if ans == c:
                return True
            if ans > c:
                r -= 1
            elif ans < c:
                l += 1
                
        return False
        
        
        