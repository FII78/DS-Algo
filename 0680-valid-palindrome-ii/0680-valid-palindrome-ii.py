class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        opt = list(s)
        need = 0
        while l < r:
            if opt[l] != opt[r]:
                s1 = opt[:l] + opt[l+1:]
                s2 = opt[:r] + opt[r+1:]
                return s1 == s1[::-1] or s2==s2[::-1]
         
            else:
                l += 1
                r -= 1
            
        return True
            
        
        