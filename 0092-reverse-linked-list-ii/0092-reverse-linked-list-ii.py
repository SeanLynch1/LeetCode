# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # since head could be what gets reversed, if we return it, we are returning the listnode that head originally pointed to, so instead make a new listNode that points to the first listNode, and return it's next, we will update what it points to but we can confirm it will always be first, head may not always be first. we are not making a copy of the current linked list, we are modifying it in place, but just adding a pointer to the first node, as the first node could change depending on where the reverse begins
        
        dummy = ListNode(0)
        dummy.next = head

        # set prev
        prev = dummy

        # iterate through the linked list until we reach the start of the reversal

        for i in range(left - 1):
            prev = prev.next

        start = prev.next
        then = start.next

        for i in range(right - left):
            # start will always equal start, just update who it points to, we want it to point to the .next of right
            start.next = then.next
            # then, who will move forward one each iteration, always will point to its previous, the reason it points to prev.next it because then moves forward one, and prev.next points to what then used to be
            then.next = prev.next

            # this step will always be wrong until the last iteration of the loop
            prev.next = then

            # move then forward to what it originally pointed to
            then = start.next
            

        return dummy.next