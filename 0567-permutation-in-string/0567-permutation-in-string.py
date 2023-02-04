class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #         SAME LENGTH AND UNIQUE CHARS MUST BE THE SAME AND THEIR FREQUECY OF THE 
#         CORRESPONDING CHARS MUST BE EQUAL
        k = len(s1)
        dict1 = Counter(s1)
        
        # initial window
        window = s2[:k]
        dict2 = Counter(window)
        # check the intial window 
        if dict1 == dict2:
            return True
  
        for i in range(len(s2)-k):
        
            # SLIDE THE WINDOW
            # 1 - remove s2[i]
            if dict2[ s2[i] ] == 1:
                del dict2[ s2[i] ]
                
            elif dict2[ s2[i] ] > 1:
                dict2[s2[i]] -= 1
            
            # 2- add s2[i+k]
            if s2[i+k] in dict2:
                dict2[s2[i+k]] += 1
            else:
                dict2[s2[i+k]] = 1
                
            # check after sliding
            if dict1 == dict2:
                return True
                
        return False
        
        
        
        