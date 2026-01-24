# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def get_num(self, node: ListNode) -> int:
        first_num = 0
        dummy_node = ListNode(0, node)
        prev = dummy_node

        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        dummy_node.next.next = None
        curr = prev
        while curr:
            first_num = (first_num * 10) + curr.val
            curr = curr.next

        return first_num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total = str(self.get_num(l1) + self.get_num(l2))
        curr = None
        dummy_node = ListNode(0)
        prev = dummy_node
        for i in range(len(total)-1, -1, -1):
            curr = ListNode(int(total[i]))
            prev.next = curr
            prev = curr
            curr = curr.next

        return dummy_node.next
        
