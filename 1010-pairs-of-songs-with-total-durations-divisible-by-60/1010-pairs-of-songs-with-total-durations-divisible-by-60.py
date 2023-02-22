class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        target = [0] * 60
        cnt = 0
        
        for t in time:
            cnt += target[(60 - (t % 60)) % 60]
            target[t % 60] += 1
            
        return cnt
    

        