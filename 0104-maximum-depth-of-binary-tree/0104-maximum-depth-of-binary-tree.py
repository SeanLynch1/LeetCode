# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        def recursiveSearch(root, level: int) -> int:
            left, right = level, level
            if root.left != None:
                left = recursiveSearch(root.left, level + 1)

            if root.right != None:
                right = recursiveSearch(root.right, level + 1)

            return max(left, right)

         
        return recursiveSearch(root, 1)

        




                