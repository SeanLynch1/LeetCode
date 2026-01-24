# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 1:
            return head

        dummy_node = ListNode(0, head)
        prev = dummy_node
        curr = head

        n = 1

        while curr:
            n += 1
            curr = curr.next

        curr = head

        while curr:
            if n - k > 0:
                start = prev
                fast = curr.next

                for _ in range(k):
                    curr.next = prev
                    prev = curr

                    curr = fast
                    if fast:
                        fast = fast.next

                    n -= 1

                temp = start.next
                temp.next = curr
                start.next = prev
                prev = temp
            else:
                break

        return dummy_node.next