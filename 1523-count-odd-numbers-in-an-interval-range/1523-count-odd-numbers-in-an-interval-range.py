class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        _range = high - low + 1
        
        if _range % 2 == 0:
            return _range//2
        
        else:
            if low % 2 and high % 2:
                return _range//2+1
            else:
                return _range-_range//2-1
                