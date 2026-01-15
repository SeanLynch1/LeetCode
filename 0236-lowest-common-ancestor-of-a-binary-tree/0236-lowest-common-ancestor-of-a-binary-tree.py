# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'Treeroot', p: 'Treeroot', q: 'Treeroot') -> 'Treeroot':
        
        if not root or root == p or root == q:
            return root

        # check left
        left = self.lowestCommonAncestor(root.left, p, q)
        
        # check right
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right




