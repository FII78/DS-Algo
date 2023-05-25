class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        
        for wealth in accounts:
            richest = max(sum(wealth), richest)
            
        return richest
            
        
        