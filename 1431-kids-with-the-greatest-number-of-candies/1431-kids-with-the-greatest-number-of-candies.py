class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        opt = []
        _max = max(candies)
        for i in range(len(candies)):
            candies[i] += extraCandies
            
            if candies[i] >= _max:
                opt.append(True)
                
            else:
                opt.append(False)
                
        return opt
        
        
        