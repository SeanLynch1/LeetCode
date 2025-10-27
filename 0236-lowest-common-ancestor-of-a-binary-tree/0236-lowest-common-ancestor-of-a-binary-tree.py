# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = root

        def helper(node: TreeNode):
            
            if not node:
                return 0

            found = 0
            if node == p or node == q:
                found += 1

            found += helper(node.left)
            found += helper(node.right)

            if found == 2:
                self.ancestor = node
                found = 0

            return found

        helper(root)

        return self.ancestor

        