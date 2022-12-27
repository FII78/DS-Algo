class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        
        i = len(nums)-1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
            
        if i == 0:
            return -1
        
        j = len(nums)-1
        
        while j > 0 and nums[i-1] >= nums[j]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = nums[-1:i-1:-1]
        ret = int(''.join(nums))
        
        return ret if ret < 1<<31 else -1
        