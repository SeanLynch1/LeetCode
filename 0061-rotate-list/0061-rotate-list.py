# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head

        node_count = 1
        curr = head

        while curr.next:
            node_count += 1
            curr = curr.next

        k = k % node_count

        if k == 0:
            return head

        mid = node_count - k
        
        temp = head
        for i in range(mid):
            tail = temp   
            temp = temp.next
        
        tail.next = None
        curr.next = head

        return temp