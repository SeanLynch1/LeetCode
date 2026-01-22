# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        node_count = len(nodes)

        if node_count == 1 or node_count == k:
            return head

        k = k % node_count
        mid = node_count - k

        if k == 0:
            return head

        right_dummy = ListNode(0, nodes[mid])

        nodes[-1].next = head
        nodes[mid - 1].next = None

        return right_dummy.next