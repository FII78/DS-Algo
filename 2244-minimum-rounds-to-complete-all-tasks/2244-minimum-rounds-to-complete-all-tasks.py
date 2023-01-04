class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        
        _min = 0
        
        for k, v in c.items():
            if v == 1:
                return -1
            _min += v//3 + bool(v%3)  
                            
        return _min
            
            
            
                
            
        