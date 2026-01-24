# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy_node = ListNode(0)
        prev = dummy_node

        while l1 or l2:

            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            total = val_1 + val_2 + carry
            carry = total // 10

            prev.next = ListNode(total % 10)
            prev = prev.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry == 1:
            prev.next = ListNode(carry)
            
        return dummy_node.next