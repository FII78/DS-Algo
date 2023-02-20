class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        _max = 0
        _min = float("inf")
        
        for i in range(len(nums)):
            _min = min(_min, nums[i])
            _max = max(_max, nums[i] - _min)
        
        return _max if _max else -1