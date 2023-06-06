class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = set()
        
        for i in range(len(arr)-1):
            diff.add(abs(arr[i+1] - arr[i]))
            
        return len(diff) == 1
        
        
        