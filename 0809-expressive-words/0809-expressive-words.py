class Solution:
    
        
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def repLeng(word, left):
            
            right = left
            while (right < len(word) and word[right] == word[left]):
                right += 1
            return right - left

        cnt = 0
        
        for word in words:
            
            i, j = 0, 0
            check = True
            
            while i < len(word) and j < len(s):
                # check if every distinct char is the same
                if word[i] != s[j]:
                    check = False
                    break
                
                repOrig = repLeng(s, j)
                repWord = repLeng(word, i)
                
                if (repWord >= repOrig or repOrig < 3) and repWord != repOrig:
                    check = False
                    break
                
                i += repWord
                j += repOrig
                
            check = (i == len(word) and j == len(s))
            
            if check:
                cnt += 1
    
        return cnt
    
    
 