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
        
        if not root:
            return root

        queue = deque([root])

        while queue:
            prev = Node()
            for i in range(len(queue)):
                
                curr = queue.popleft()
                prev.next = curr

                # add left
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

                prev = curr

        return root
