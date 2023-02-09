class Solution:
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        """
        Normal sliding techinques and keep incrementing the right value untill it's number of 
        distinct is greater than k.
        
        approach:
        
        Maintain a counter dictionary, left & right pointer and output variable
        
        sliding window:
        1. valid ( expand untill number of distinct elements are less than K): incremet right pointer
        2. invalid ( shrink while number of distinct elements are greater than K): increment left pointer
        
        if valid:
            add the size of the sub array to our output
        else:
            decrement the value at the left pointer from the counter dictionary: if it's 0 remove it
            increment left pointer
        
        Since we're adding the whole size of each subarray we can do the same thing but with K-1:
            Meaning now we have all the valid subarrays: goodarrays(K most) - goodarrays(K-1): 
            1, 2, 3 = K
            1, 2 = K-1
            removing the count of K-1 good arrays from the count of K good arrays will give exactly K

        """
         
        counter = defaultdict(int)

        left, outputK = 0, 0

        for right, num in enumerate(nums):
            counter[num] += 1

            while len(counter) > k:
                counter[nums[left]] -= 1

                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1

            outputK += right - left + 1
            
        counter = defaultdict(int)    
        left, outputK2 = 0, 0

        for right, num in enumerate(nums):
            counter[num] += 1

            while len(counter) > k-1:
                counter[nums[left]] -= 1

                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
 
            outputK2 += right - left + 1

        return outputK - outputK2
    
                
                
                
                
                
                
        
        