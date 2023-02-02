class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        Question comes down to counting the number of ways we can chose three
        numbers from the string where no consecutive numbers are equal.
        
        value E {0,1}
        
        so all the possible combinations using 0 and 1 are:
        
        000
        001
        010
        100
        110
        101
        111
        
        From this possible combinations only "010" and "101" are valid since they don't 
        contain cosecutive 0's or 1's.
        
        From position side, we have 3 possiblities for both 0 and 1.
        Postions E {0,1,2} ... since we only choose length 3 subsequences
        
        Therefore, if we have a 2D list:
        
        valid[value][position]
        Test case: s = "001101", where se is seen
        
        v p  se
        0 0  1 2 2 2 3 3
          1  0 0 0 0 2 2
          2  0 0 0 0 4 4
        
        1 0  0 0 1 2 2 3
          1  0 0 2 4 4 3
          2  0 0 0 0 0 2
        
        - A value becomes as a first element everytime we see it.
        valid[0][0] += 1 
        valid[1][0] += 1
        
        - A value becomes as a second element:
            if it's '0', we've seen '1' as a first element, same for 1
            // how many cases are there where other value is a first element
            
            valid[0][1] += valid[1-0][0] = valid[1][0] 
            valid[1][1] += valid[1-1][0] = valid[0][0]
            
        - A value becomes as a third element:
            if it's '0', we've seen '1' as a second element, same for 1
            // how many cases are there where other value is a second element
            
            valid[0][2] += valid[1-0][1] = valid[1][1] 
            valid[1][2] += valid[1-1][1] = valid[0][1]
        
        Time complexity: O(N), where is the length of string and we're only doing 3 operations 
        Space complexity: O(1), since it's 3x2 matrix
        
        """
        
        valid = [[0] * 3 for _ in range(2)]
     
        
        for value in map(lambda c: int(c), s):
            valid[value][0] += 1
            valid[value][1] += valid[1-value][0]
            valid[value][2] += valid[1-value][1]
            
        return valid[0][2] + valid[1][2]
            
            