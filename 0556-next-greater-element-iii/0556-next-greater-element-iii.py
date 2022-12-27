class Solution:
    def output(self, nums, n):
        opt = int("".join(list(map(str, nums))))
        if opt <= 2 ** 31 - 1 and opt > n:
            return opt
        else:
            return -1
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(int,str(n)))
        
        i = len(nums)-1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
            
        if i == 0:
            nums.reverse()
            return self.output(nums, n)
           
        
        j = len(nums)-1
        
        while j > 0 and nums[i-1] >= nums[j]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = nums[-1:i-1:-1]
        return self.output(nums, n)
        