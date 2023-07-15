class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        sort by start time
        take/not take for each event
        
        knowing which one is the next event????
        if current eending time is 3 i've to find the nearest starting time 
        """
        n = len(events)        
        events.sort()
        dp = [[-1] * (k + 1) for _ in range(n) ]
        _start = [start for start,_,_ in events]
        
        def dfs(i, count):
            if i == n or count == 0:
                return 0
            if dp[i][count] != -1:
                return dp[i][count]
            
            next_start = bisect_right(_start, events[i][1])
            
            not_take = dfs(i+1, count)
            take = events[i][2] + dfs(next_start, count-1)
            dp[i][count] = max(take, not_take)
            
            return dp[i][count]
        
        return dfs(0, k)