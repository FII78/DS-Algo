class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c = Counter(arr)
        print(c)
        for num in arr:
            if num == 0:
                if c[0] > 1:
                    return True
            elif c[num*2]:
                return True
            
        return False    
        
                
        