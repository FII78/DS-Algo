class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            if ((i == 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                cnt += 1
                
        return cnt >= n
   
       