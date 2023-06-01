class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        
        for i in nums:
            if not len(str(i)) % 2:
                cnt += 1
        return cnt
        