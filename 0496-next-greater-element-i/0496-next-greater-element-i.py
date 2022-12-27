class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        di = defaultdict(int)
        
        for i,n in enumerate(nums2):
            j = i+1
            
            while j < len(nums2) and nums2[j] < nums2[i]:
                j += 1
            if j == len(nums2):
                di[n] = -1
            else:
                di[n] = nums2[j]
      
        
        res = [-1] * len(nums1)
        for i,n in enumerate(nums1):
            res[i] = di[n]

        return res
                
        
                
                
        
        