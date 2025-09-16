# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        string_left = []
        string_right = []

        curr = l1
        while curr:
            string_left.append(str(curr.val))
            curr = curr.next

        string_left = string_left[-1::-1]
        string_left = int(''.join(string_left))

        curr = l2
        while curr:
            string_right.append(str(curr.val))
            curr = curr.next

        string_right = string_right[-1::-1]
        string_right = int(''.join(string_right))

        total = str(string_left + string_right)

        head = ListNode(int(total[-1]))
        curr = head

        for i in range(len(total) - 2, -1, -1):
            curr.next = ListNode(int(total[i]))
            curr = curr.next

        return head


