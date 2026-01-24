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
            
        mapping = {}
        curr = head
        copy = None

        while curr:
            if curr not in mapping:
                mapping[curr] = Node(curr.val)

            if copy:
                copy.next = mapping[curr]

            copy = mapping[curr]

            if curr.random:
                if curr.random not in mapping:
                    mapping[curr.random] = Node(curr.random.val)

                copy.random = mapping[curr.random]
                
            print(f"curr = {copy.val}", end = ", ")
            if copy.random:
                print(f"it points to {copy.random.val}")
            else:
                print(f"it points to {copy.random}")
                
            curr = curr.next
            print("\n")

        return mapping[head]