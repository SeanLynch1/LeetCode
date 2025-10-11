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
        # preorder -> node left right
        curr = root 

        while curr:
            
            temp_right = curr.right

            if curr.left:
                # find the deepest piece on the right side
                deepest_right = curr.left

                while deepest_right.right:
                    deepest_right = deepest_right.right

                curr.left, curr.right = None, curr.left
                deepest_right.right = temp_right

                curr = curr.right
            else:
                curr = curr.right


        return root