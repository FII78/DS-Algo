class Solution:
    def validPalindrome(self, s: str) -> bool:
        def delete(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            return True
               
        cnt = 0
        
        l,r = 0, len(s)-1
        
        while l <= r:
            if s[l] != s[r]:
                return delete(s, l+1, r) or delete(s, l, r-1)  
            l += 1
            r -= 1
            
        return True
                
            
        