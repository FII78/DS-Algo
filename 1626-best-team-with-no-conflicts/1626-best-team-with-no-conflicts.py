class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
         
            persons = [(ages[i],scores[i]) for i in range(len(ages))]
            persons.sort(reverse=True)
            
            dp = [0 for _ in range(len(persons))]
            best = 0
            for i in range(len(persons)):
                dp[i] = persons[i][1]
                for j in range(i):
                    if persons[i][1] <= persons[j][1]:
                        dp[i] = max(dp[i],dp[j]+persons[i][1])
                
           
            return max(dp)
            
            
        