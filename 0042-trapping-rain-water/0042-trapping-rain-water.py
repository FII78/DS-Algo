class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n < 3:
            return 0
        
        maxLeft = [0] * n
        maxRight = [0] * n
        opt = 0
        left = float("-inf")
        for i in range(n):
            if i == 0:
                left = max(left, height[i])
                continue
            else:
                left = max(left, height[i])
                maxLeft[i] += left
                
        right = float("-inf")
        for i in reversed(range(n)):
            if i == 0:
                right = max(right, height[i])
                continue
            else:
                right = max(right, height[i])
                maxRight[i] += right
                
        for i in range(n):
            diff = min(maxLeft[i], maxRight[i]) - height[i]
            if diff > 0:
                opt += diff
        return opt
            
        
        
        