class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
          
            if str(x)[-1] != 0:
                res = -1 * int((str(x)[:0:-1]))
                if (res >= 2 ** 31 - 1 or res <= -2 ** 31):
                    return 0 
                else: 
                    return res
 
                  
        else:
            res = int(str(x)[::-1])
            if (res >= 2 ** 31 - 1 or res <= -2 ** 31):
                return 0 
            else: 
                return res