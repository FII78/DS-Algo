class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        opt = [-1] * len(nums)
        stack = []
        
        for i in range(2*len(nums)):
            i = i % len(nums)
            
            while stack and nums[i] > stack[-1][1]:
                idx, num = stack.pop()
                opt[idx] = nums[i]
            stack.append([i, nums[i]])
        return opt
            
        
        