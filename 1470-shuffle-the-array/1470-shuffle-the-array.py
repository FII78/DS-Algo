class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        opt = []
        
        for i in range(n):
            opt.append(nums[i])
            opt.append(nums[i+n])
        return opt
        