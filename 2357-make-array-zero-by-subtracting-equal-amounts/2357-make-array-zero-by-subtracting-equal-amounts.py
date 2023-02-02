class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        coll = set()
        
        for n in nums:
            if n != 0:
                coll.add(n)
                
        return len(coll)
        
        
        