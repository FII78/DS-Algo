# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseList(head):
            prev = None
            curr = head
            _next = None
        
            while curr:
                _next = curr.next
                curr.next = prev
                prev = curr
                curr = _next
            
            return prev
        l1 = reverseList(l1)
        l2 = reverseList(l2)
         
     
        
        dummy = ListNode()
        curr = dummy
        
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            curr = curr.next                
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
    
        return reverseList(dummy.next)
        
        
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        