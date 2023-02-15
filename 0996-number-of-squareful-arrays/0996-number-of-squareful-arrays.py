class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        perm = []

        def dfs(nums, path):
            if not nums:
                perm.append(path)
                return 

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                if path and not self.check(path[-1] + nums[i]):
                    continue

                temp = path.copy()
                temp.append(nums[i])
                dfs(nums[:i] + nums[i + 1:], temp)
                
        nums.sort()
        dfs(nums, [])
        
        return len(perm)

    def check(self,num):
        return sqrt(num) == int(sqrt(num))
        