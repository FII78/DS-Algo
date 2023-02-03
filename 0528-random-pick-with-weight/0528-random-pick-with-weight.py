

class Solution:
    
    """
    [1,2,4]
    
    prob: 1 + 2 + 4 = 7
    
    1/7 , 2/7, 4/7
    
    since it's the sum we can take the prefix/cumulative sum
    
    0,1,3,7 ... the diff is still the orig numbers
    we can pick a random number from 1 to the max(7)... so we just have to find 
    which range is the random number
    ranges: 0..1 , 1..3, 3..7
              1.     2.    4
    if rand = 4, we know it's. range is between 3 and 7, but we have to do linear search to find it's range. but instead of that we can do in logn time using binary 
    search.
    
    """

    def __init__(self, w: List[int]):
        self.cumlative_sum = [0]
        self.w = w
        
        for num in w:
        # calculating the cumnulative sum
            self.cumlative_sum.append(self.cumlative_sum[-1] + num)
         
        self.cumlative_sum = self.cumlative_sum[1:] # remove temp 0
       
    def pickIndex(self) -> int:
        _max = self.cumlative_sum[-1] # the last sum is the maximum sum
        rand = random.randint(1, _max) #find the a random number between 1 and the max
        idx = bisect.bisect_left(self.cumlative_sum, rand) #binary search to find the it's place in the cumulative sum
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()