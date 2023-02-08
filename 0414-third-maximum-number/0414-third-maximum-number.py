import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) <= 2:
            return max(nums)
        heap = []
        
        for i in nums:
            heap.append(-1 * i)
        heapq.heapify(heap)
    
        for i in range(2):
            heapq.heappop(heap)
            
        return -1*heap[0]