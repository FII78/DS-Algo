class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        Approach 1
        
        Relative order of digit logs can be maintained
        
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero"
        
        dig1: 8 1 5 1 
        let1: art can
        dig2: 3 6
        let2: own kit dig
        let3: art zero
        
        if digit in value: add it to digit dictionary
        if not: add it to a separate array and sort it finally and then
        conactinate it with the digit array for result
        
        digit_dict: dig1: 8 1 5 1, "dig2 3 6"
        letter_list: "let1 art can"
        
        Approach 2:
        
        Instead of sorting it, push it to heap as a tuple (remaining, identifier)
        to sort it lexicographically
        
        
        
        """
        digit_logs = []
        letter_logs = []
        heap = []
        
        for log in logs:
            curr = log.split(" ")
            
            #collect digit logs in a seprate array
            if curr[1].isnumeric():
                digit_logs.append(log)
            
            else:
                remaining = ' '.join(curr[1:])
                identifier = curr[0]
                heapq.heappush(heap, (remaining, identifier))
        
        for _ in range(len(heap)):
            remaining, identifier = heapq.heappop(heap) 
            letter_logs.append(' '.join([identifier, remaining]))
        
        return letter_logs + digit_logs
            

         
        
        