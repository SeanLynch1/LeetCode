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
        print(curr.val)

        count = 0
        while curr:
            curr.seen = True
            curr = curr.next

            if curr:
                print(curr.val)
            
            count += 1

            if count >= 10001:
                return True

        return False