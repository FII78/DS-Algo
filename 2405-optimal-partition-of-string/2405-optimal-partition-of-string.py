class Solution:
    def partitionString(self, s: str) -> int:
        seen = [-1] * 26
        count = 1
        substring_idx = 0
        
        for i in range(len(s)):
            if seen[ord(s[i]) - ord('a')] >= substring_idx:
                count += 1
                substring_idx = i
            seen[ord(s[i]) - ord('a')] = i
            
        return count
        
        