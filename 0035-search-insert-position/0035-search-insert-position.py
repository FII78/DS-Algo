class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def left_bs(target):
            l,r = 0, len(nums)
            
            while l < r:
                mid = (l+r) // 2

                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        return left_bs(target)