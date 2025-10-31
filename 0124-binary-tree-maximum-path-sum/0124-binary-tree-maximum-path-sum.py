# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = root.val

        def helper(node: TreeNode) -> int:

            if not node:
                return 0
            
            val = node.val

            left = max(helper(node.left), 0) # 30
            right = max(helper(node.right), 0) # 4
            
            self.max_sum = max(left + right + val, self.max_sum)

            outcome = val + max(left, right) # 39

            return outcome

        helper(root)
        return self.max_sum
