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
                right_most_start = curr.left

                while right_most_start:
                    while right_most_start.right:
                        right_most_start = right_most_start.right

                    if not right_most_start.left:
                        right_most_start.right = curr.right
                        curr.left, curr.right = None, curr.left
                        curr = curr.right
                        right_most_start = None
                    else:
                        right_most_start.left, right_most_start.right = None, right_most_start.left
                        right_most_start = right_most_start.right


            else:
                curr = curr.right


