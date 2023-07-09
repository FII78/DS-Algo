class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        _min = float("inf")
        _sum = 0
        
        while r < len(nums):
            _sum += nums[r]
            
            while _sum >= target:
                _min = min(_min, r-l+1)
                _sum -= nums[l]
                l += 1 
            r += 1
            
        return _min if _min != float(inf) else 0