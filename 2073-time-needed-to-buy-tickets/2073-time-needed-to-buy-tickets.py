class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0
        
        for idx, ticket in enumerate(tickets):
            if idx > k:
                cnt += min(tickets[k]-1, ticket)
            else:   
                cnt += min(ticket, tickets[k])
                
        return cnt
       