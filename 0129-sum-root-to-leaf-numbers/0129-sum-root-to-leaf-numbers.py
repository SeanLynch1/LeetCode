# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root: TreeNode, value: int) -> int:
            if not root.left and not root.right:
                return root.val + value

            val = 0

            if root.left:
                val += dfs(root.left, (value + root.val) * 10)

            if root.right:
                val += dfs(root.right, (value + root.val) * 10)
            
            return val

        return dfs(root, 0)