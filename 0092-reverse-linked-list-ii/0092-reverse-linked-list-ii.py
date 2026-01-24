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

        curr = head
        prev = dummy_node

        idx = 1
        while curr:
            if idx == left:
                start = prev
                fast = curr.next
                for _ in range(right - left + 1):
                    
                    curr.next = prev
                    prev = curr

                    curr = fast
                    if fast:
                        fast = fast.next

                start.next.next = curr
                start.next = prev
                break

            prev = curr
            curr = curr.next
            idx += 1

        return dummy_node.next





