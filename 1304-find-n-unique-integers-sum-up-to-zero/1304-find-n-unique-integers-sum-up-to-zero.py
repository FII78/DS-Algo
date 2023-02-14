class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        even = False if n%2 else True
        n=n//2+1
        
        for i in range(1, n):
            arr.append(-i)
        if not even:   
            arr.append(0)
        
        for i in range(1, n):
            arr.append(i)
        return arr
        
        