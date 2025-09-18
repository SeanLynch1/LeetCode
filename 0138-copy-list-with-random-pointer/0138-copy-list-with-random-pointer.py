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
        idx = 1

        while curr:
            randoms[curr] = idx

            new = Node(curr.val)
            indexes[-1].next = new
            indexes.append(new)

            curr = curr.next
            idx += 1
    
        for i, node in enumerate(randoms):
            n = node.random
            if n in randoms:
                n = randoms[n]
                indexes[i].random = indexes[n]     

        return indexes[0]