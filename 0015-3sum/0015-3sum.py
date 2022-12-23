class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        opt = []
        nums.sort()
        
        for i,x in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = len(nums)-1
       
            while j < k:
                temp = nums[j] + nums[k] + nums[i]
                if temp == 0:
                    opt.append([x,nums[j],nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif temp > 0:
                    k -= 1
                else:
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    
        return opt
                
        