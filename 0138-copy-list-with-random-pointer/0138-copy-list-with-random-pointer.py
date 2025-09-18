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
    
        print("randoms = ", randoms, "\n")     

        for i, node in enumerate(randoms):
            print(i)
            if node.random in randoms:
                node.random = randoms[node.random]
                indexes[i].random = indexes[node.random]     

        for i, node in enumerate(indexes):
            print(f"i = {i}, node.val = {node.val}, node.next = {node.next}, node.random = {node.random}")

        print("\n")
        for node, index in randoms.items():
            print(f"idx = {index}, val = {node.val}, next = {node.next}, random = {node.random}","\n")

        return indexes[0]