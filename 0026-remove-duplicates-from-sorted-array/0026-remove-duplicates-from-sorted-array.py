class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        cnt = set()
        for right in range(len(nums)):
            if nums[right] in cnt:
                continue
            nums[left] = nums[right]
            cnt.add(nums[right])
            left += 1
            
        return left
        
        