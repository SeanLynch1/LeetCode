# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # begin by finding first occurance of node with val x

        curr = head

        left_end = ListNode(0, curr)
        head = left_end

        mid_point = None

        while curr:
            if curr.val >= x:
                mid_point = curr
                break
            
            left_end = curr
            curr = curr.next
        
        right_end = mid_point

        while curr:
            start = curr
            if curr.val >= x:
                right_end = curr
            else:
                right_end.next = curr.next
                left_end.next = curr

                curr.next = mid_point
                left_end = curr

            curr = start.next

        return head.next

        