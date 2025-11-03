# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.lca = root

        def helper(node) -> int:

            if node == None:
                return 0

            found = 0
            if node == p or node == q:
                found += 1


            left = helper(node.left)
            right = helper(node.right)

            num = left + right + found
            print(f"node = {node.val}, num = {num}")
            if num == 2:
                self.lca = node
                return 0

            return num


        helper(root)
        return self.lca