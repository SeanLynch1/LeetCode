# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.min_diff = float('inf')

        self.last_val = None
        # inorder traversal
        def helper(node: TreeNode) -> int:
            if not node:
                return

            helper(node.left)

            if self.last_val is not None:
                diff = abs(self.last_val - node.val)
                self.min_diff = min(self.min_diff, diff)

            self.last_val = node.val

            helper(node.right)

            return

        
        helper(root)
        return self.min_diff