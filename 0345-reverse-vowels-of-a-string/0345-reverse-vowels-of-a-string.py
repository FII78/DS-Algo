class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        vowel = ("a", "e", "i", "o", "u","A", "E", "I", "O", "U")        
        opt = list(s)
        
        while l < r:
            while l < r and opt[l] not in vowel:
                l += 1
            while l < r and opt[r] not in vowel:
                r -= 1
            opt[l], opt[r] = opt[r], opt[l]
            l += 1
            r -= 1
            
        return "".join(opt)
        
       