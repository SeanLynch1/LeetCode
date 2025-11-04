# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        left_depth = 0
        left_curr = root.left

        while left_curr:
            left_depth += 1
            left_curr = left_curr.left

        right_depth = 0
        right_curr = root.right

        while right_curr:
            right_depth += 1
            right_curr = right_curr.left

        # left side is perfect (possibly)
        if left_depth == right_depth:
            return self.countNodes(root.right) + (2 ** left_depth)
            
        # right side is perfect (possibly)
        else:
            return self.countNodes(root.left) + (2 ** right_depth)
