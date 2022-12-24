class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pairs = []
        
        nums.sort()
        l,r = 0, len(nums)-1
        
        while l < r:
            pairs.append(nums[l] + nums[r])
            l += 1
            r -= 1
        return max(pairs)
        
        