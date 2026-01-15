# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.path = float('-inf')

        def traverse(root: TreeNode) -> int:
            if not root:
                return 0

            me = root.val
            # evaluate left
            left = traverse(root.left)

            # evaluate right
            right = traverse(root.right)

            self.path = max(self.path, me)
            self.path = max(self.path, max(left + me, right + me))
            self.path = max(self.path, left + me + right)

            return max(me, max(left + me, right + me))

        traverse(root)
        return self.path
