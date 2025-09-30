class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            # If we’re at the start of a duplicate run
            if curr.next and curr.val == curr.next.val:
                val = curr.val
                # Skip the entire run
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                # No duplicate → keep it
                prev = prev.next
                curr = curr.next

        return dummy.next
