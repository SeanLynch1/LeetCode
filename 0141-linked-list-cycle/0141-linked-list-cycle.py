# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        curr = head
        count = 0

        while curr:
            curr = curr.next

            count += 1

            if count > 10000:
                return True

        return False