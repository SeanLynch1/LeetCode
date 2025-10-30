# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.sum = 0

        def helper(node: TreeNode, predecessor: int) -> int:
            if not node:
                return
                
            predecessor += node.val

            if not node.left and not node.right:
                self.sum += predecessor
                return

            predecessor *= 10

            helper(node.left, predecessor)

            helper(node.right, predecessor)

            return

        helper(root, 0)

        return self.sum

