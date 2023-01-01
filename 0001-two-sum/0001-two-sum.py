class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = set()
        
        for i, v in enumerate(nums):
            if target - v in pairs:
                return [i, nums.index(target-v)]
            else:
                pairs.add(v)
            
        