"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mapping = {}
        curr = head
        dummy_node = Node(0)
        copy = dummy_node

        while curr:
            if curr not in mapping:
                mapping[curr] = Node(curr.val)

            copy.next = mapping[curr]
            copy = copy.next

            if curr.random:
                if curr.random not in mapping:
                    mapping[curr.random] = Node(curr.random.val)

                copy.random = mapping[curr.random]

            curr = curr.next

        return dummy_node.next