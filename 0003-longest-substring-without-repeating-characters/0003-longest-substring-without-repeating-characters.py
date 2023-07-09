class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        l,r = 0,0
        seen = set()
        
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            seen.add(s[r])
            _max = max(_max, r-l+1)
            r += 1
        return _max