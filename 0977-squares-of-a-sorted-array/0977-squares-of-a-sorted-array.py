class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        output = []
        while l <= r:
            if abs(nums[l]) <= abs(nums[r]):
                output.append(nums[r] * nums[r])
                r -= 1
            else:
                output.append(nums[l] * nums[l])
                l += 1
                
        return output[::-1]
            
        