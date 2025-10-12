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

            combined = left_side + right_side
            max_side = max(left_side, right_side)
            largest = max(combined + node.val, max_side + node.val)

            
            self.optimal_sum = max(largest, self.optimal_sum)

            return max_side
        
        helper(root)
        return self.optimal_sum
