# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prev = head
        count = 0

        while prev:
            prev = prev.next
            count += 1

        prev = dummy
        
        for i in range(count // k):
            start = prev.next
            then = start.next

            for i in range(k - 1):
                start.next = then.next
                then.next = prev.next
                prev.next = then
                then = start.next
            
            prev = start

        return dummy.next