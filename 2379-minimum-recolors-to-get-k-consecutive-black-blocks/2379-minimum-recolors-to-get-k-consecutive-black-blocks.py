class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #Sliding window
        
        l = -1
        _min = float("inf")
        white_cnt = 0
        
        for r, c in enumerate(blocks):
            if c == "W":
                white_cnt += 1
            if r - l == k:
                _min = min(white_cnt, _min)
                l += 1
                if blocks[l] == "W":
                    white_cnt -= 1
              
        return _min
                
        