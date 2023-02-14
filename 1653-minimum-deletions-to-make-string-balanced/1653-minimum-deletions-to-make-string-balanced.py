class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        
        s = "aababbab"
        balance s: (i,j) i<j and s[i]="b" and s[j] = "a"
        if we see any "b" that means following that, there should no be an 
        "a", so flag if b is seen
        """
        
        min_del = 0
        flag_b = 0
        
        for c in s:
            if c == 'a' and not flag_b:
                continue
            elif c == 'b':
                flag_b += 1
            elif flag_b and c == 'a':
                min_del += 1
                flag_b -= 1
                
        return min_del
                
        