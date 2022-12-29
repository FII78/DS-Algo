class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flips = []
        
        for i in range(n):
            curr_max = max(arr[0:n-i])
            idx = arr.index(curr_max)
            
            arr[:idx+1] = reversed(arr[:idx+1])
            flips.append(idx+1)
            
            arr[:n-i] = reversed(arr[:n-i])
            flips.append(n-i)
        return flips
    
            
                
                