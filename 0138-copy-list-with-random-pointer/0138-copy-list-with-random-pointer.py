class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mapping = {}

        dummy = Node(0)
        copy_curr = dummy
        curr = head

        while curr:
            # create copy for current node unconditionally
            copy = Node(curr.val)
            mapping[curr] = copy

            copy_curr.next = copy
            copy_curr = copy

            curr = curr.next

        # second pass to assign random pointers
        curr = head
        copy_curr = dummy.next

        while curr:
            if curr.random:
                copy_curr.random = mapping[curr.random]

            curr = curr.next
            copy_curr = copy_curr.next

        return dummy.next
