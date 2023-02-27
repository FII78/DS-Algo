class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        pop = 1
        _maxCnt = float("-inf")
        logs = sorted(logs)
        
        for i in range(len(logs)):
            cnt = 0
            
            for j in range(len(logs)):
                if logs[j][0] <= logs[i][0] and logs[j][1] > logs[i][0]:
                    cnt += 1
                    
            if cnt > _maxCnt:
                _maxCnt = cnt
                pop = logs[i][0]
                
        return pop
        