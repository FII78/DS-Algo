class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        prev = 0
        for i in nums:
            arr.append(prev + i)
            prev += i
        return arr
        
        
        