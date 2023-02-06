class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        
        for word in words:
            if len(word) >= len(pref) and (pref == word or pref == word[:len(pref)]):
                cnt += 1
                
        return cnt
                
        