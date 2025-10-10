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

        curr = root
        
        while curr:
            
            if curr.left:

                right_most = curr.left

                while right_most.right:
                    right_most = right_most.right

                right_most.right = curr.right
                curr.left, curr.right = None, curr.left

            curr = curr.right

        return root