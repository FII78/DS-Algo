class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l, r = 0, len(num)-1
        
        while l < r:
            _sum = num[l] + num[r]
            
            if _sum < target:
                l += 1
            elif _sum > target:
                r -= 1
            else:
                return [l+1, r+1]
        