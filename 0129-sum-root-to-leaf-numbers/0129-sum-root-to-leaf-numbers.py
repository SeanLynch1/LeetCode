# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        def helper(node: TreeNode, predecessor: int) -> int:
            if not node:
                return 0

            predecessor = predecessor * 10 + node.val

            if not node.left and not node.right:
                return predecessor
                
            return helper(node.left, predecessor) + helper(node.right, predecessor)

        return  helper(root, 0)

