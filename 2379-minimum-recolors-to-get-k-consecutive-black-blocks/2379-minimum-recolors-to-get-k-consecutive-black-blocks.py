class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #counting the number of "W"s in range of every K and finding the minimum number of "W"s overall.
        
        _min = float("inf")
        
        for i in range(len(blocks) - k + 1):
            white_cnt = blocks.count('W', i, i + k)
            _min = min(white_cnt, _min)
        
        return _min
                
        