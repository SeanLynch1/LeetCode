# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        left_head = None
        right_head = None
        temp = head
        left = None
        right = None

        while temp:
            if temp.val >= x:
                if right_head == None:
                    right_head = temp
                    right = right_head
                else:
                    right.next = temp
                    right = right.next
            else:
                if left_head == None:
                    left_head = temp
                    left = left_head
                else:
                    left.next = temp
                    left = left.next
                
            temp = temp.next

        if right:
            right.next = None
        if left:
            left.next = right_head

        return left_head if left_head is not None else right_head
