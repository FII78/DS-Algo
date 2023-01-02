class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap = sum(1 for c in word if c.isupper())
        
        if cap == len(word) or cap == 0:
            return True
        
        if cap == 1 and word[0].isupper():
            return True
        
        return False
        
            
        
        