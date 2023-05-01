class Solution:
    def average(self, salary: List[int]) -> float:
        _min = min(salary)
        _max = max(salary)
        tot = 0
        
        for n in salary:
            if n != _min and n != _max:
                tot += n
        return tot / (len(salary)-2)
                
        
        