# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_path = root.val

        def helper(node: TreeNode) -> int:
            if not node:
                return 0

            if not node.left and not node.right:
                self.max_path = max(self.max_path, node.val)
                return node.val

            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            self.max_path = max(self.max_path, left + right + node.val)

            return max(left + node.val, right + node.val)
        
        helper(root)

        return self.max_path