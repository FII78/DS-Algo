class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        opt = []
        nums.sort()
        quad = []
        
        def kSum(k, start, target):
            
            if k!=2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
            else:
                c,d = start, len(nums)-1

                while c < d:
                    if nums[c] + nums[d] > target:
                        d -= 1
                
                    elif nums[c] + nums[d] < target:
                        c += 1
                        while nums[c] == nums[c-1] and c < d:
                            c += 1
                    else:
                        opt.append(quad + [nums[c],nums[d]])
                        c += 1
                        while nums[c] == nums[c-1] and c < d:
                            c += 1
        kSum(4, 0, target)
        return opt
                        
                
        
        