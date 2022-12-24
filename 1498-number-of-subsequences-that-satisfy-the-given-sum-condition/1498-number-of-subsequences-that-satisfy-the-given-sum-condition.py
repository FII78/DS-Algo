class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        MOD =10**9 + 7
        res = 0
        l,r = 0,n-1

        for l in range(n):
            while r >= l and nums[l]+nums[r] > target:
                r -= 1

            if r >= l and nums[l] + nums[r] <= target:
                res += pow(2,(r-l),MOD)
                 
        return res % MOD       
        
       