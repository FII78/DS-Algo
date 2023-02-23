class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.append(1)
        nums.insert(0,1)
        
        @cache
        def dfs(i, j):
            if i > j:
                return 0
            _min = float("-inf")
            for k in range(i,j+1):
                cost = nums[i-1] * nums[j+1] * nums[k]
                cost += dfs(i, k-1) + dfs(k+1, j) 
                _min = max(cost, _min)
            return _min

        return dfs(1, len(nums)-2)