# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)

        left = left_dummy
        right = right_dummy

        while head:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            head = head.next

        right.next = None
        left.next = right_dummy.next

        return left_dummy.next


        