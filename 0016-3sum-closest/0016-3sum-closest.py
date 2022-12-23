class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        _minDiff = float("inf")
        _minSum = 0
        
        nums.sort()
        
        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i+1, len(nums)-1
            
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                curr = abs(target-_sum)
                if curr == 0:
                    return target
                if _minDiff > curr :
                    _minDiff = curr
                    _minSum = _sum
                if _sum > target:
                    k -= 1
                    
                else:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                
        return _minSum
        