# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        dummy_node = ListNode(0, head)
        prev = dummy_node
        curr = head
        difference = 1
        # we need to track how far away the current node is to the reference node
        n += 1
        while curr:
            if difference == n:
                prev = prev.next
                difference -= 1

            curr = curr.next
            difference += 1

        prev.next = prev.next.next
        
        return dummy_node.next