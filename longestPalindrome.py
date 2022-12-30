class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l , r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1
            
        L, R = 0, 0
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            if odd[1] - odd[0]  > (R - L):
                L =  odd[0]
                R =  odd[1]
            if even[1] - even[0] > (R - L):
                L =  even[0]
                R =  even[1]
      
        return s[L:R+1]