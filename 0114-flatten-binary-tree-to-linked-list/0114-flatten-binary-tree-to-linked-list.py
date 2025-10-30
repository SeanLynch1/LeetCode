# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        stack = []
        curr = root

        while stack or curr:
            
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()

            while not curr.right and stack:
                parent = stack.pop()

                next_node = parent.right
                parent.right = parent.left
                parent.left = None

                curr.right = next_node
                    
            curr = curr.right

        return root
                


