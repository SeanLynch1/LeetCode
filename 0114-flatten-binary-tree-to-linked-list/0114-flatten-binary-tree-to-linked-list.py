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
        prev = None

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()

            if curr.left:
                prev.right = curr.right
                curr.left, curr.right = None, curr.left
                curr = prev.right
            else:

                prev = curr
                
                curr = curr.right
               
            