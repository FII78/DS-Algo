class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0,len(s)-1
        opt = list(s)
        while l < r:
            while l < r and not opt[l].isalpha():
                l += 1
            while l < r and not opt[r].isalpha():
                r -= 1
            opt[l], opt[r] = opt[r], opt[l]
            l += 1
            r -= 1
            
        return "".join(opt)
        