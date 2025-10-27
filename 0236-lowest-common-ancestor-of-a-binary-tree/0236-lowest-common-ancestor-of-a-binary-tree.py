# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case
        if not root or root == p or root == q:
            return root

        # Recurse into left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are found in different branches, root is their LCA
        if left and right:
            return root

        # Otherwise, return whichever side is non-null (propagate up)
        return left if left else right
