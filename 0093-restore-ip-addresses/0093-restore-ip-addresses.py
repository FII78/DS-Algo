class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # edge case
        if len(s) < 4 or len(s) > 12:
            return []
        
        self.answer = []
        
        def backtrack(index, arr):
            # if current idx is at the last index or if I length of arr is 4
            if index == len(s) or len(arr) == 4:
                #check if index is at last and len(arr) == 4 (valid)
                if index == len(s) and len(arr) == 4:
                    self.answer.append(".".join(arr))
                return
            
            for i in range(index, min(index+3, len(s))):
                if i == index:
                    temp = arr.copy()
                    temp.append(s[index:i+1])
                    backtrack(i+1, temp)
                
                elif s[index] != "0" and int(s[index: i+1]) <= 255:
                    temp = arr.copy()
                    temp.append(s[index:i+1])
                    backtrack(i+1, temp)
                # else:
                #     return 
               
                
        backtrack(0, [])
        return self.answer
  
                        
            
            
                