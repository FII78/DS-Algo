# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        _len = 0
        temp = head
        while temp:
            temp = temp.next
            _len += 1
        k = _len-n
        if k == 0:
            return head.next
        i = 0
        node = head
        while i < k - 1:
            node = node.next
            i += 1
        node.next = node.next.next
        return head