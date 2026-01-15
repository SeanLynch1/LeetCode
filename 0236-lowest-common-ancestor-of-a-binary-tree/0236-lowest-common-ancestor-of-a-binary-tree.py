# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.lca = root

        def dfs(node: TreeNode, p: TreeNode, q: TreeNode) -> int:
            
            if not node:
                return 0

            found = 0

            if node == p or node == q:
                found += 1

            # check left
            found += dfs(node.left, p, q)
            
            if found == 2:
                self.lca = node
                found = 0
                
            # check right
            found += dfs(node.right, p, q)

            if found == 2:
                self.lca = node
                found = 0

            return found

        dfs(root,p,q)

        return self.lca



