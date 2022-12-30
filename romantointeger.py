class Solution:
    def romanToInt(self, s: str) -> int:
     
        
#         I - V and X
#         X - L and C
#         C - D and M
        
        hashT = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100,'D':500,'M': 1000}
        opt = 0
        
        for i,n in enumerate(s):
            if i + 1 < (len(s)) and hashT[s[i+1]] > hashT[n]:
                opt -= hashT[n]
            else:
                opt += hashT[n]
            
        return opt