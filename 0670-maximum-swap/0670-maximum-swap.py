class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        num = 27
              for 2 look for max greater in the right
              72
              
        num = 727
              for 7 look for greater if there's not greater for to the next 
              pos to find greater
       
        """
        num = list(str(num))
        
        swap = 0
        for i, v in enumerate(num):
            _max, max_idx = int(v), i
            
            for j in range(len(num)-1, i, -1):
                if int(num[j]) <= _max:
                    continue
                else:
                    _max = int(num[j])
                    max_idx = j
                    swap = 1
            if swap == 1:
                num[i], num[max_idx]  = str(_max), num[i]
                break
                
        return int("".join(num))
    
            
            
                    
                
        
        
        