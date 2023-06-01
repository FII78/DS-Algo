class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        
        cnt = 0
        _maxlen = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                cnt += 1
                
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
                
            _maxlen = max(_maxlen, right - left + 1)
            
        return _maxlen
                
        
        
                
        
            
                
        
        