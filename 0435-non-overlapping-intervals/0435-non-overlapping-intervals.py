class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [1,2] [1,3] [2,3] [3,4] 
 
        
        
        """
        
        intervals.sort(key = lambda x: x[1])
        ans = 0
        recent_end = float("-inf")
        
        for start, end in intervals:
            # if my current start is greater than or equal to last end - no overlap
            if start >= recent_end:
                recent_end = end
            #overlap: update ans since we're removing the current interval to have more choices
            else:
                ans += 1
                
        return ans
                
        
        