# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.lca = root

        def dfs(node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            
            if not node or node == p or node == q:
                return node

            # check left
            left = dfs(node.left, p, q)
            
            # check right
            right = dfs(node.right, p, q)

            if left and right:
                return node

            return left or right

        return dfs(root,p,q)




