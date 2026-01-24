# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        mapping = {}

        dummy_node = ListNode(-101, head)
        mapping[-1] = dummy_node

        curr = head
        key = 0
        while curr:
            mapping[key] = curr
            key += 1
            curr = curr.next
        
        n = len(mapping) - n - 1
        print(f"n = {n}")
        print(f"mapping = {mapping}")
        mapping[n-1].next = mapping[n].next

        return dummy_node.next