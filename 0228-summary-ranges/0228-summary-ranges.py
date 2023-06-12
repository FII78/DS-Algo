class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        curr = []
        
        for i in range(len(nums)):
            if not curr or (nums[i] - curr[-1] == 1):
                curr.append(nums[i])
            elif nums[i] - curr[-1] != 1:
                ranges.append([curr[0], curr[-1]])
                curr = []
                curr.append(nums[i])
        if len(curr) >= 1:
            ranges.append([curr[0],curr[-1]])
        
        opt = []
        
        for num in ranges:
            if num[0] != num[1]:
                opt.append(str(num[0]) + "->" + str(num[1]))
            else:
                opt.append(str(num[0]))
                
        return opt
            
            
            
        
        