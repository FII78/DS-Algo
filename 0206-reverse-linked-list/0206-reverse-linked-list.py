# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        _next = None
        
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
            
        return prev
        
        


        
        