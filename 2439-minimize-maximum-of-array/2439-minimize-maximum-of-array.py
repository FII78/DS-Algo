class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _min = nums[0]
        total = nums[0]
        
        for i in range(1, len(nums)):
            total += nums[i]
            _min = max(_min, ceil(total/(i+1)))
        return _min
        