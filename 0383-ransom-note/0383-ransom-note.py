class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        
        for char, cnt in ransomNote.items():
            if magazine[char] < cnt:
                return False
            
        return True
        