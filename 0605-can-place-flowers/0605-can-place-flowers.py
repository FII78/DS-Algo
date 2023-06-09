class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        _len = len(flowerbed)
        
        for i in range(_len):
            if flowerbed[i] == 0:
                empty_left = ( i==0 ) or (flowerbed[i-1] == 0)
                empty_right = ( i==(_len-1)) or (flowerbed[i+1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    cnt += 1
        return cnt >= n
        