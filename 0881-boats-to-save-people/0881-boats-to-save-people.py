class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        _min = 0
        nums.sort()
        
        l,r = 0, len(nums)-1
        
        while l <= r:
            _sum = nums[l] + nums[r]
            
            if _sum > limit:
                _min += 1
            else:
                _min += 1
                l += 1
            r -= 1
            
        return _min
        
        