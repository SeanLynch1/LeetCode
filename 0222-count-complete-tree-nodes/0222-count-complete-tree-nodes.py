# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        while root:
            root = root.left
            depth += 1

        return depth


    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        
        if left_depth == right_depth:
            return self.countNodes(root.right) + 2 ** left_depth
        else:
            return self.countNodes(root.left) + 2 ** right_depth

        
        