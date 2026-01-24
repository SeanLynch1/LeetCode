# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head

        dummy_node = ListNode(0, head)
        prev = dummy_node

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        next_node = None

        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = next_node
            next_node = curr
            curr = tmp

        prev.next.next = curr
        prev.next = next_node

        return dummy_node.next





