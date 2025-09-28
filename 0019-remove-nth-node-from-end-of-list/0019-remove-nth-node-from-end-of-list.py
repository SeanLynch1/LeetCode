# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        # keep a gap of n + 1 between fast and slow
        for i in range(n + 1):
            fast = fast.next
        
        # great, now fast is the correct distance ahead of slow

        # move fast to the very end, once this has been achieve, we know slow is one before the node that needs to be removed
        while fast:
            fast = fast.next
            slow = slow.next


        # okay so now jut update slow.next to skip its current and point straight to its next

        slow.next = slow.next.next

        return dummy.next