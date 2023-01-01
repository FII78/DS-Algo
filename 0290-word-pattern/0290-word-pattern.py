class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(words) != len(pattern) or len(set(words)) != len(set(words)):
            return False
        
        follow = [-1] * 26
        
        for i in range(len(pattern)):
            char = ord(pattern[i]) - ord('a')
            word = words[i]
            
            if follow[char] != -1:
                if follow[char] != word:
                    return False
            else:
                for j in range(26):
                    if follow[j] == word:
                        return False
                follow[char] = word
        return True
  