# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # post order -> left right node
        # 9, 15, 7, 20, -10

        self.optimal_sum = root.val

        def helper(node: Optional[TreeNode]) -> int:
            
            if not node:
                return 0

            left_side = max(helper(node.left), 0)
            right_side = max(helper(node.right), 0)

            self.optimal_sum = max(node.val + left_side + right_side, self.optimal_sum)

            return max(left_side, right_side) + node.val
        
        helper(root)
        return self.optimal_sum
