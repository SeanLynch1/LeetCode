class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # map original -> copy
        mapping = {}

        # First pass: create all new nodes
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: assign next and random pointers
        curr = head
        while curr:
            if curr.next:
                mapping[curr].next = mapping[curr.next]
            if curr.random:
                mapping[curr].random = mapping[curr.random]
            curr = curr.next

        return mapping[head]
