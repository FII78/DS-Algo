class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        
        """
        if not nums or k == 0:
            return 0
        
        cnt = 0
        prefix = 0  
        _dic = {0:1}  
        
        for num in nums:
            prefix += num
            rem = prefix % k
            
            if rem < 0:
                rem += k
                
            if rem in _dic:
                cnt += _dic[rem]
                
            if rem not in _dic:
                _dic[rem] = 1
                
            else:
                _dic[rem] += 1
                
        return cnt
