class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        
        i = 0
        _len = 0
        curr_line = []
        
        while i < len(words):
            word = words[i]
            
            if _len + len(word) <= maxWidth:
                curr_line.append(word)
                _len += len(word) + 1
                i += 1
            else:
                spaces = maxWidth - _len + len(curr_line)
                placed = 0
                idx = 0
                while placed < spaces:
                    if idx >= len(curr_line) - 1:
                        idx = 0
                    curr_line[idx] +=  " "
                    placed += 1
                    idx += 1
                    
                output.append("".join(curr_line))
                curr_line = []
                _len = 0
                
        for i in range(len(curr_line)  - 1):
            curr_line[i] += " "
        
        curr_line[-1] += " " * ( maxWidth - _len + 1)
        output.append("".join(curr_line))
        
        return output