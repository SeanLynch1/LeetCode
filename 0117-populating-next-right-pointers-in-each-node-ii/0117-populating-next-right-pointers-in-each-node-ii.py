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
        
        curr = root

        while curr:

            dummy_node = TreeNode()
            dummy_node.next = curr
            temp = curr.left

            while temp and curr:
                if curr.left and temp != curr.left:
                    temp.next = curr.left
                    temp = temp.next
                elif curr.right:
                    temp.next = curr.right
                    temp = temp.next
                    
                curr = curr.next

            curr = dummy_node.next.left

        return root
            
