# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.lca = root

        def helper(node: TreeNode) -> bool:
            if not node:
                return False

            if node == p or node == q:
                self.lca = node
                return True

            left = helper(node.left)
            right = helper(node.right)

            if left and right:
                self.lca = node

            return (left or right)

        helper(root)

        return self.lca

