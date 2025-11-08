# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.output = 0
        self.k = k

        def helper(node: Optional[TreeNode], k: int):

            if not node:
                return

            # inorder traversal
            # -> left node right

            # search left
            helper(node.left, k)

            self.k -= 1

            if self.k == 0:
                self.output = node.val
                return

            # search right
            helper(node.right, k)

        helper(root, self.k)

        return self.output
