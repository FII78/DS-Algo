class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        _max = float("-inf")
        prev = 0
        
        for i in gain:
            _max = max(_max, (i+prev), prev)
            prev = i+prev
        return _max      