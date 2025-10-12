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

            self.optimal_sum = max(node.val, self.optimal_sum)

            left_side = max(helper(node.left), 0)
            right_side = max(helper(node.right), 0)

            combined = node.val + left_side + right_side
            max_side = max(left_side + node.val, right_side + node.val)
            largest = max(combined, max_side)
            self.optimal_sum = max(largest, self.optimal_sum)

            return max_side
        
        final = helper(root)
        return max(final, self.optimal_sum)
