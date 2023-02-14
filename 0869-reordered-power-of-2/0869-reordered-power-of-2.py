class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
    
        c = Counter(str(n))
        
        for i in range(30):
            pt = str(1 << i)
            if c == Counter(pt):
                return True
        return False

        
        