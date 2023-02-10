class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = []
        new.extend(nums1)
        new.extend(nums2)
        new.sort()
        new = sorted(new)
        n = len(new)
        idx = (n - 1) // 2
    
        if (n % 2):
            return new[idx]
        else:
            return (new[idx] + new[idx + 1])/2.0
       