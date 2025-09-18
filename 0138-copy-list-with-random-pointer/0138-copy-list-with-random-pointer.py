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
            return head

        indexes = [Node(head.val)]
        randoms = {head : 0}

        curr = head.next

        while curr:
            randoms[curr] = len(indexes)

            new = Node(curr.val)
            indexes[-1].next = new
            indexes.append(new)

            curr = curr.next

        for i, node in enumerate(randoms):
            if node.random in randoms:
                node.random = randoms[node.random]
                indexes[i].random = indexes[node.random]     

        return indexes[0]