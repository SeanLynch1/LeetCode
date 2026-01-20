"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        parent = root

        dummy = Node(0)
        dummy.next = parent

        while parent:
            
            child = None

            while parent:

                if parent.left:
                    if not child:
                        child = parent.left
                        dummy.next = child
                    else:
                        child.next = parent.left
                        child = child.next

                if parent.right:
                    if not child:
                        child = parent.right
                        dummy.next = child
                    else:
                        child.next = parent.right
                        child = child.next

                parent = parent.next

            parent = dummy.next
            dummy.next = None

        return root


            
