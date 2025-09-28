# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = {}

        curr = head
        count = 1

        while curr:
            nodes[count] = curr
            curr = curr.next
            count += 1

        for key, value in nodes.items():
            print(key, value, "\n")
        print("count = ", count)
        if (count - n - 1) > 0:
            if (count-n-1 + 2) in nodes:
                nodes[count - n - 1].next = nodes[count-n-1 + 2]
            else:
                nodes[count - n - 1].next = None
        else:
            return nodes[1].next

        return head